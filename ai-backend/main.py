"""
FastAPI backend for NeuroMaze: Adaptive Puzzleverse
Handles difficulty adjustment based on player emotion.
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class EmotionRequest(BaseModel):
    """Request model for emotion input."""
    emotion: str

@app.post("/adjust-difficulty/")
def adjust_difficulty(request: EmotionRequest):
    """Adjusts game difficulty based on the provided emotion."""
    emotion = request.emotion
    difficulty = "Normal"  # Default difficulty
    # Adjust logic based on emotion
    if emotion == "Happiness":
        difficulty = "Easy"
    elif emotion == "Anger":
        difficulty = "Hard"
    else:
        difficulty = "Normal"
    feedback = f"Difficulty adjusted to {difficulty} based on {emotion}"
    return {"difficulty": difficulty, "feedback": feedback}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
