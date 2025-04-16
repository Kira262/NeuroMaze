@echo off
echo Testing NeuroMaze Installation
echo ============================

REM Check Python environment
echo Checking Python environment...
python --version
if %errorlevel% neq 0 (
    echo [ERROR] Python not found
    exit /b 1
)

REM Check virtual environment
echo Checking virtual environment...
if not exist .venv (
    echo [ERROR] Virtual environment not found
    exit /b 1
)

REM Activate virtual environment
call .venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo [ERROR] Failed to activate virtual environment
    exit /b 1
)

REM Check required packages
echo Checking required packages...
python -c "import fastapi, uvicorn, torch, cv2, mediapipe" 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Some required packages are missing
    exit /b 1
)

REM Check webcam access
echo Checking webcam access...
python -c "import cv2; cap = cv2.VideoCapture(0); ret, _ = cap.read(); cap.release(); exit(0 if ret else 1)" 2>nul
if %errorlevel% neq 0 (
    echo [WARNING] Webcam not accessible
)

REM Check backend health
echo Checking backend health...
curl -s http://localhost:8000/health >nul 2>&1
if %errorlevel% equ 0 (
    echo [INFO] Backend is running
) else (
    echo [INFO] Backend is not running (this is normal if not started)
)

echo.
echo Installation test complete!
echo All checks passed successfully.
echo.
pause 