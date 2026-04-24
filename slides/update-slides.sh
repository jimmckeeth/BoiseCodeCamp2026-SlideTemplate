#!/bin/bash

# update-slides.sh - Linux/macOS wrapper
set -e

# Check for Python 3
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    rm -f .dependencies-installed # Ensure we re-install if venv was just created
fi

# Install/Update dependencies if marker file is missing
if [ ! -f ".dependencies-installed" ]; then
    echo "Ensuring dependencies are installed..."
    ./venv/bin/pip install --quiet python-pptx cairosvg Pillow
    touch .dependencies-installed
fi

# macOS specific: cairosvg might need cairo via brew
if [[ "$OSTYPE" == "darwin"* ]]; then
    if ! command -v brew &> /dev/null; then
        echo "Note: If script fails, install Homebrew and 'brew install cairo'"
    elif ! brew list cairo &> /dev/null; then
        echo "Installing system dependency: cairo..."
        brew install cairo
    fi
fi

# Run the script
./venv/bin/python update_slides.py
