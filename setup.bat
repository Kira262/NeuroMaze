@echo off
echo Setting up NeuroMaze environment...
echo ================================

REM Check Python version
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

REM Get Python version
for /f "tokens=2" %%a in ('python --version') do set PYTHON_VERSION=%%a
for /f "tokens=1 delims=." %%a in ("%PYTHON_VERSION%") do set MAJOR_VERSION=%%a
for /f "tokens=2 delims=." %%a in ("%PYTHON_VERSION%") do set MINOR_VERSION=%%a

REM Check if Python version is compatible
if %MAJOR_VERSION% LSS 3 (
    echo Python version %PYTHON_VERSION% is not supported. Please install Python 3.8 or higher.
    pause
    exit /b 1
)
if %MAJOR_VERSION% EQU 3 if %MINOR_VERSION% LSS 8 (
    echo Python version %PYTHON_VERSION% is not supported. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

REM Check if pip is installed
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo pip is not installed. Please install pip.
    pause
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist .venv (
    echo Creating virtual environment...
    python -m venv .venv
    if %errorlevel% neq 0 (
        echo Failed to create virtual environment.
        pause
        exit /b 1
    )
)

REM Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment.
    pause
    exit /b 1
)

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip
if %errorlevel% neq 0 (
    echo Failed to upgrade pip.
    pause
    exit /b 1
)

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install dependencies.
    pause
    exit /b 1
)

echo.
echo Setup complete! You can now run the game using 'launch.bat'
echo.
echo Available commands:
echo - launch.bat    : Start the game
echo - run_game.bat  : Run the game (if already set up)
echo - cleanup.bat   : Reset the environment
echo.
pause 