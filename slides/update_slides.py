import os
import random
import glob
import json
import re
from pptx import Presentation
from pptx.util import Inches, Pt
import cairosvg
from io import BytesIO

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def find_target_info(prs, target_text):
    """Finds the bounding box of the target text in slide masters or layouts."""
    for master in prs.slide_masters:
        for shape in master.shapes:
            if shape.has_text_frame and target_text in shape.text:
                return shape
        for layout in master.slide_layouts:
            for shape in layout.shapes:
                if shape.has_text_frame and target_text in shape.text:
                    return shape
    return None

def get_luminance(hex_color):
    """Calculates relative luminance of a hex color."""
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 3:
        hex_color = ''.join([c*2 for c in hex_color])
    try:
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        return (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255
    except:
        return 0.5

def adjust_svg_colors(svg_text, mode):
    """Adjusts colors in SVG if it appears to be a single-color logo."""
    if mode not in ["lighten", "darken"]:
        return svg_text

    # Find all hex colors
    colors = set(re.findall(r'#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})', svg_text))
    
    # Check for fill="black" or similar named colors or style="fill:black"
    named_colors = set(re.findall(r'fill[:=]["\']?(black|white|#000|#fff)["\']?', svg_text.lower()))
    
    # If no colors found, it's likely default black
    if not colors and not named_colors:
        if mode == "lighten":
            # Add a global style to make it white
            return svg_text.replace('<svg ', '<svg fill="white" ')
        return svg_text

    # Simple heuristic: if there's only one unique color (or very similar colors)
    all_found = colors.union(named_colors)
    if len(all_found) <= 2: # Allow for a color and maybe its shadow/stroke
        for c in colors:
            lum = get_luminance(c)
            if mode == "lighten" and lum < 0.3:
                svg_text = re.sub(f'#{c}', '#FFFFFF', svg_text, flags=re.IGNORECASE)
            elif mode == "darken" and lum > 0.7:
                svg_text = re.sub(f'#{c}', '#000000', svg_text, flags=re.IGNORECASE)
        
        # Handle named colors
        if mode == "lighten":
            svg_text = svg_text.replace('fill="black"', 'fill="white"').replace('fill:black', 'fill:white')
            svg_text = svg_text.replace('fill="#000"', 'fill="#fff"').replace('fill="#000000"', 'fill="#ffffff"')
        elif mode == "darken":
            svg_text = svg_text.replace('fill="white"', 'fill="black"').replace('fill:white', 'fill:black')
            svg_text = svg_text.replace('fill="#fff"', 'fill="#000"').replace('fill="#ffffff"', 'fill="#000000"')

    return svg_text

def get_image_data(logo_path, cache, adjust_mode):
    """Loads image data, converting SVG to PNG if necessary, with caching."""
    cache_key = f"{logo_path}_{adjust_mode}"
    if cache_key in cache:
        return cache[cache_key]
    
    try:
        if logo_path.endswith(".svg"):
            with open(logo_path, "r", encoding="utf-8", errors="ignore") as f:
                svg_text = f.read()
            
            if adjust_mode != "none":
                svg_text = adjust_svg_colors(svg_text, adjust_mode)
            
            blob = cairosvg.svg2png(bytestring=svg_text.encode('utf-8'))
            data = BytesIO(blob)
        else:
            with open(logo_path, "rb") as f:
                data = BytesIO(f.read())
        cache[cache_key] = data
        return data
    except Exception as e:
        print(f"  Warning: Failed to load {logo_path}: {e}")
        return None

def should_skip_slide(slide, skip_text):
    """Checks if the first line of speaker notes matches the skip text."""
    if not slide.has_notes_slide:
        return False
    notes = slide.notes_slide.notes_text_frame.text.strip().lower()
    if not notes:
        return False
    first_line = notes.split('\n')[0].strip()
    return first_line == skip_text.lower()

def generate_progress_bar_text(pct, width=20):
    """Generates a text-based progress bar like ▓▓▓░░ 15%."""
    filled = int(width * pct)
    empty = width - filled
    return f"{'▓' * filled}{'░' * empty} {int(pct*100)}%"

def process_presentation():
    config = load_config()
    pptx_path = config["input_pptx"]
    logos_dir = config["logos_dir"]
    target_text = config["target_text"]
    num_logos_requested = config["num_logos_per_slide"]
    output_path = config["output_pptx"]
    skip_notes = config.get("skip_notes", "Keep this slide")
    randomize = config.get("random_logos", True)
    add_pb = config.get("add_progress_bar", False)
    pb_text = config.get("progress_bar_text", "Progress bar")
    pb_width = config.get("progress_bar_width", 20)
    adjust_mode = config.get("adjust_logos", "none")

    if not os.path.exists(pptx_path):
        print(f"Error: {pptx_path} not found.")
        return

    prs = Presentation(pptx_path)
    
    # 1. Handle the logo placeholder
    target_shape = find_target_info(prs, target_text)
    if target_shape:
        left, top, width, height = target_shape.left, target_shape.top, target_shape.width, target_shape.height
        target_shape.text = "" # Clear the template text
        is_vertical = height > width
        print(f"Detected {'vertical' if is_vertical else 'horizontal'} logo orientation.")
    else:
        print(f"Warning: Could not find logo placeholder text box with '{target_text}'.")
        left = top = width = height = None

    logo_files = glob.glob(os.path.join(logos_dir, "*.svg")) + glob.glob(os.path.join(logos_dir, "*.png"))
    image_cache = {}
    
    total_slides = len(prs.slides)
    print(f"Processing {total_slides} slides...")

    pb_regex = re.compile(r"([▓░]{2,} \d+%)|" + re.escape(pb_text))

    for i, slide in enumerate(prs.slides):
        progress_pct = (i + 1) / total_slides
        
        # --- Progress Bar Logic ---
        if add_pb:
            new_pb_str = generate_progress_bar_text(progress_pct, pb_width)
            for shape in slide.shapes:
                if shape.has_text_frame:
                    if pb_regex.search(shape.text):
                        shape.text = pb_regex.sub(new_pb_str, shape.text)

        # --- Logo Logic ---
        if should_skip_slide(slide, skip_notes):
            print(f"  Skipping slide {i+1} logos (Speaker notes match: '{skip_notes}')")
            continue

        if left is not None:
            if randomize:
                selected = random.sample(logo_files, min(num_logos_requested, len(logo_files)))
            else:
                start_idx = (i * num_logos_requested) % len(logo_files)
                selected = logo_files[start_idx : start_idx + num_logos_requested]

            num_to_fit = len(selected)
            if is_vertical:
                avail_per_logo = height / num_to_fit
                if avail_per_logo < Inches(0.1): # Safety limit
                    num_to_fit = int(height / Inches(0.1))
                    avail_per_logo = height / num_to_fit
                    selected = selected[:num_to_fit]
            else:
                avail_per_logo = width / num_to_fit
                if avail_per_logo < Inches(0.1):
                    num_to_fit = int(width / Inches(0.1))
                    avail_per_logo = width / num_to_fit
                    selected = selected[:num_to_fit]

            current_offset = 0
            for logo_path in selected:
                img_data = get_image_data(logo_path, image_cache, adjust_mode)
                if not img_data: continue
                img_data.seek(0)
                
                pic = slide.shapes.add_picture(img_data, 0, 0)
                aspect_ratio = pic.width / pic.height
                
                if is_vertical:
                    max_w, max_h = width * 0.9, avail_per_logo * 0.9
                    if (max_w / max_h) > aspect_ratio:
                        pic.height = int(max_h); pic.width = int(max_h * aspect_ratio)
                    else:
                        pic.width = int(max_w); pic.height = int(max_w / aspect_ratio)
                    pic.left = int(left + (width - pic.width) / 2)
                    pic.top = int(top + current_offset + (avail_per_logo - pic.height) / 2)
                else:
                    max_w, max_h = avail_per_logo * 0.9, height * 0.9
                    if (max_w / max_h) > aspect_ratio:
                        pic.height = int(max_h); pic.width = int(max_h * aspect_ratio)
                    else:
                        pic.width = int(max_w); pic.height = int(max_w / aspect_ratio)
                    pic.left = int(left + current_offset + (avail_per_logo - pic.width) / 2)
                    pic.top = int(top + (height - pic.height) / 2)

                current_offset += avail_per_logo

    prs.save(output_path)
    print(f"\nSuccess! Saved to {output_path}")

if __name__ == "__main__":
    process_presentation()
