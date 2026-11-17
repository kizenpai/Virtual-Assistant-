@echo off
title EDITH AI Virtual Assistant
color 0B

echo ======================================================================
echo                 EDITH - AI-Powered Virtual Assistant
echo               B.Tech Artificial Intelligence Lab Project
echo ======================================================================
echo.

:: Detect Python executable - Prioritize Anaconda environment with installed packages
if exist "D:\anaconda3\python.exe" (
    set PY_CMD=D:\anaconda3\python.exe
    goto RUN
)

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    set PY_CMD=python
    goto RUN
)

if exist "C:\Python311\python.exe" (
    set PY_CMD=C:\Python311\python.exe
    goto RUN
)

echo [ERROR] Python was not found on your system PATH!
echo Please ensure Python 3.10+ is installed and added to PATH.
pause
exit /b 1

:RUN
echo Launching EDITH Virtual Assistant using %PY_CMD%...
echo.
"%PY_CMD%" main.py %*

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [NOTE] If you encountered an error, you can also test in CLI mode:
    echo "%PY_CMD%" main.py --cli
    pause
)

