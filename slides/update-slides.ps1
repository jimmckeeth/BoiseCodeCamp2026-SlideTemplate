# update-slides.ps1 - Windows wrapper
$ErrorActionPreference = "Stop"

# Check for Python
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Error "Error: Python is not installed or not in PATH."
    return
}

# Create virtual environment if it doesn't exist
if (!(Test-Path "venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
    if (Test-Path ".dependencies-installed") { Remove-Item ".dependencies-installed" }
}

# Install/Update dependencies if marker file is missing
if (!(Test-Path ".dependencies-installed")) {
    Write-Host "Ensuring dependencies are installed..."
    & ".\venv\Scripts\pip.exe" install --quiet python-pptx cairosvg Pillow
    New-Item -Path ".dependencies-installed" -ItemType File > $null
}

# Run the script
Write-Host "Running update_slides.py..."
& ".\venv\Scripts\python.exe" update_slides.py

Write-Host "`nPress any key to exit..."
$null = [Console]::ReadKey()
