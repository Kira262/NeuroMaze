@echo off
echo NeuroMaze Cleanup
echo ================

REM Stop any running processes
taskkill /F /IM python.exe /FI "WINDOWTITLE eq NeuroMaze*" >nul 2>&1

REM Remove virtual environment
if exist .venv (
    echo Removing virtual environment...
    rmdir /s /q .venv
)

REM Remove __pycache__ directories
echo Cleaning Python cache...
for /d /r . %%d in (__pycache__) do @if exist "%%d" rmdir /s /q "%%d"

REM Remove .pytest_cache if it exists
if exist .pytest_cache rmdir /s /q .pytest_cache

echo Cleanup complete! You can now run setup.bat to start fresh.
pause 