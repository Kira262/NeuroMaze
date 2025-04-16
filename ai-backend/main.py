from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()


class PlayerData(BaseModel):
    puzzle_time: float
    error_rate: float
    emotion: str


@app.post("/adjust-difficulty/")
def adjust_difficulty(player_data: PlayerData):
    """
    Adjust puzzle difficulty based on player data (time, errors, emotion).
    """
    # Simple logic to adjust difficulty
    difficulty = "Normal"

    if player_data.emotion == "Frustrated" or player_data.error_rate > 0.5:
        difficulty = "Easy"
    elif player_data.puzzle_time > 60:
        difficulty = "Hard"

    return {"difficulty": difficulty, "feedback": "Keep going!"}


@app.get("/")
def read_root():
    return {"message": "NeuroMaze API is running!"}
