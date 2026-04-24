# Boise Code Camp (BCC) Presentation Tools

A collection of cross-platform automation tools for PowerPoint decoration and session timing.

---

## 1. PowerPoint Slide Decorator

A system to randomly decorate PowerPoint slides with logos and a dynamic progress bar.

### Features
- **Logo Randomization**: Automatically finds a placeholder text area in your Slide Master or Layouts and fills it with random logos from a local folder.
- **Orientation Awareness**: Detects if the logo area is vertical or horizontal and layouts logos accordingly without overlapping.
- **Progress Bar**: Replaces a footer text placeholder with a Unicode-based progress bar (e.g., `▓▓▓░░ 30%`). It is idempotent and can be recalculated if the script is run again.
- **Smart Color Adjustment**: Automatically "lighten" dark single-color SVG logos for dark themes or "darken" light ones.
- **Slide Skipping**: Skips slides if the first line of speaker notes matches a specific string (default: "Keep this slide").
- **Auto-Environment**: Automatically creates a Python virtual environment and installs required dependencies (`python-pptx`, `cairosvg`, `Pillow`).

### Usage
1.  **Configure**: Open `config.json` and set your paths and preferences.
2.  **Run**:
    - **Windows**: Right-click `update-slides.ps1` and select "Run with PowerShell".
    - **Linux/macOS**: Run `./update-slides.sh` in your terminal.

---

## 2. Always-on-Top Session Timer

A lightweight, distraction-free countdown timer that stays on top of all windows (including PowerPoint presentations).

### Features
- **Always on Top**: Never gets hidden behind your slides.
- **Stealth Mode**: Launches with no console/taskbar window (only the timer itself).
- **Visual Alerts**: 
  - **Blink Once**: Numbers turn yellow at a configurable threshold (e.g., 10 minutes left).
  - **Blink Continuous**: Numbers toggle yellow/white every second at a final threshold (e.g., 5 minutes left).
  - **Finished**: Turns red and plays a system sound at 00:00.
- **Themed**: Clean, bold white text on a dark background.

### Usage (Windows Only)
1.  **Run**: Double-click `session-timer.vbs`.
2.  **Configure**: Right-click `session-timer.vbs`, select "Edit", and change the variables at the top:
    - `totalMinutes`: Starting duration.
    - `blinkOnceAt`: When to show the first warning.
    - `blinkEverySecondAt`: When to start the final countdown warning.

---

## Prerequisites
- **Python 3.7+** (for Slide Decorator).
- **Windows** (for Session Timer).
- **macOS Users**: `cairosvg` requires `cairo`. The script will attempt to install it via Homebrew (`brew install cairo`) if available.
