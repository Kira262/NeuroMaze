from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("neuro_maze")

# In-memory state
state = {"difficulty": "Normal", "feedback": "Waiting for data..."}


class EmotionInput(BaseModel):
    puzzle_time: float
    error_rate: float
    emotion: str


@app.post("/adjust-difficulty/")
async def adjust_difficulty(data: EmotionInput):
    logger.info(f"Received: {data}")
    # --- your existing logic ---
    if data.emotion in ["Anger", "Sadness", "Fear"] or data.error_rate > 0.4:
        diff, fb = "Easy", "You seem stressed. Taking it easy..."
    elif (
        data.emotion == "Happiness" and data.error_rate < 0.2 and data.puzzle_time < 60
    ):
        diff, fb = "Hard", "You’re on fire—cranking up the challenge!"
    else:
        diff, fb = "Normal", "Keep going!"

    # update shared state
    state["difficulty"] = diff
    state["feedback"] = fb
    logger.info(f"State updated: {state}")
    return state


@app.get("/state/")
async def get_state():
    # Unity will call this
    return state
