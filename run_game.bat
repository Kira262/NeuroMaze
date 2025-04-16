@echo off
echo Starting NeuroMaze...

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Start the game
python main.py

pause 