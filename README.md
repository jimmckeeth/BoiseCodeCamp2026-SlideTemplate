# Boise Code Camp 2026 Slide Template & Tools

This repository contains the official slide templates for Boise Code Camp 2026, along with automation tools to help speakers decorate their presentations and manage session timing.

## Repository Structure

- `slides/`: Contains the PowerPoint templates and automation scripts.
  - `BoiseCodeCamp2026.pptx`: The primary template.
  - `update_slides.py`: Python script to randomize logos and add a progress bar.
  - `session-timer.vbs`: A Windows "Always on Top" countdown timer.
  - `logos/`: A collection of SVG and PNG logos for slide decoration.
- `00-Thank-You.png`, `01-Schedule.png`, `02-SessionFeedback.png`: Standard presentation assets.

---

## 🛠 Automation Tools

Located in the `slides/` directory, these tools are designed to make slide management easier.

### 1. PowerPoint Slide Decorator
A cross-platform system to randomly decorate slides with logos and a dynamic progress bar.

- **Logo Randomization**: Fills a placeholder area (identified by text like "Insert random logos here") with random logos.
- **Progress Bar**: Automatically replaces footer text with a Unicode-based progress bar (e.g., `▓▓▓░░ 30%`).
- **Smart Formatting**: Detects area orientation (vertical/horizontal) and automatically adjusts logo colors (lighten/darken) for theme compatibility.
- **Usage**:
  - **Windows**: Right-click `update-slides.ps1` -> "Run with PowerShell".
  - **Linux/macOS**: Run `./update-slides.sh`.

### 2. Always-on-Top Session Timer (Windows)
A lightweight countdown timer that stays visible over your presentation.

- **Stealthy**: No console or taskbar window.
- **Visual Warnings**: Changes color and blinks when time is running low.
- **Usage**: Double-click `session-timer.vbs` to start. Edit the file to change duration or blink thresholds.

---

## Prerequisites

- **Python 3.7+**: Required for the Slide Decorator.
- **Windows**: Required for the Session Timer.
- **macOS**: `cairosvg` requires `cairo` (`brew install cairo`).

For detailed configuration options, see the [slides/README.md](slides/README.md).
