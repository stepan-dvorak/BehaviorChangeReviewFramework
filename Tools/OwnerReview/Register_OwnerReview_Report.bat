@echo off
setlocal
cd /d "%~dp0\..\.."
python Tools\OwnerReview\Register_OwnerReview_Report.py %*
exit /b %errorlevel%
