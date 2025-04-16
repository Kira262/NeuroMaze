"""
FastAPI backend for NeuroMaze: Adaptive Puzzleverse
Handles difficulty adjustment based on player emotion.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


class EmotionRequest(BaseModel):
    """Request model for emotion input."""

    emotion: str


class DifficultyResponse(BaseModel):
    """Response model for difficulty adjustment."""

    difficulty: str
    feedback: str
    status: str = "success"


@app.post("/adjust-difficulty/", response_model=DifficultyResponse)
def adjust_difficulty(request: EmotionRequest) -> Dict[str, Any]:
    """Adjusts game difficulty based on the provided emotion."""
    emotion = request.emotion
    difficulty = "Normal"  # Default difficulty

    # Adjust logic based on emotion
    if emotion == "Happiness":
        difficulty = "Easy"
    elif emotion == "Anger":
        difficulty = "Hard"
    elif emotion == "Fear":
        difficulty = "Easy"
    elif emotion == "Sadness":
        difficulty = "Easy"
    elif emotion == "Surprise":
        difficulty = "Normal"
    elif emotion == "Disgust":
        difficulty = "Hard"
    else:  # Neutral
        difficulty = "Normal"

    feedback = f"Difficulty adjusted to {difficulty} based on {emotion}"
    return {"difficulty": difficulty, "feedback": feedback, "status": "success"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app, host="0.0.0.0", port=8000
    )  # Changed to 0.0.0.0 to allow external connections
