@echo off
echo NeuroMaze Launcher
echo =================

REM Check if virtual environment exists
if not exist .venv (
    echo Virtual environment not found. Running setup...
    call setup.bat
    if %errorlevel% neq 0 (
        echo Setup failed. Please check the error messages above.
        pause
        exit /b 1
    )
)

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Check if backend is already running
curl -s http://localhost:8000/health >nul 2>&1
if %errorlevel% equ 0 (
    echo Backend is already running.
) else (
    echo Starting backend...
    start /B cmd /c "python main.py"
    echo Waiting for backend to start...
    timeout /t 5 /nobreak >nul
)

REM Start the game
echo Starting NeuroMaze...
python main.py

pause 