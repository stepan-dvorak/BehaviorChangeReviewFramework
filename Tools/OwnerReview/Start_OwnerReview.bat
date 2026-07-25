@echo off
setlocal
cd /d "%~dp0"

where python >nul 2>nul
if errorlevel 1 (
    echo ERROR: python was not found on PATH.
    exit /b 1
)

start "" "http://127.0.0.1:8765/"
echo Orden OwnerReview is available at http://127.0.0.1:8765/
echo Press Ctrl+C to stop the local server.
python -m http.server 8765 --bind 127.0.0.1
if errorlevel 1 exit /b 1
