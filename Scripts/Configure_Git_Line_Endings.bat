@echo off
setlocal

for /f "delims=" %%I in ('git rev-parse --show-toplevel 2^>nul') do set "REPO_ROOT=%%I"
if not defined REPO_ROOT (
    echo ERROR: Run this script from inside the Orden Git repository.
    exit /b 1
)

cd /d "%REPO_ROOT%"

git config --local core.autocrlf false || exit /b 1
git config --local core.eol lf || exit /b 1
git config --local core.safecrlf true || exit /b 1

echo Configured repository-local Git line-ending settings:
echo - core.autocrlf=false
echo - core.eol=lf
echo - core.safecrlf=true

echo.
python Scripts\Validate_Line_Endings.py --root .
exit /b %errorlevel%
