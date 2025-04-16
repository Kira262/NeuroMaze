"""
Main script to coordinate the emotion detector and backend services for NeuroMaze.
This script starts both the FastAPI backend and the emotion detector in separate threads.
"""
import threading
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from emotion_detector.emotion_detector import EmotionDetector
import time
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(title="NeuroMaze Backend")

class EmotionRequest(BaseModel):
    """Request model for emotion input."""
    emotion: str

class DifficultyResponse(BaseModel):
    """Response model for difficulty adjustment."""
    difficulty: str
    feedback: str
    status: str = "success"

@app.post("/adjust-difficulty/", response_model=DifficultyResponse)
def adjust_difficulty(request: EmotionRequest):
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
    logger.info(feedback)
    return {
        "difficulty": difficulty,
        "feedback": feedback,
        "status": "success"
    }

def run_backend():
    """Run the FastAPI backend server."""
    logger.info("Starting backend server on http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)

def run_emotion_detector():
    """Run the emotion detector in continuous mode."""
    logger.info("Starting emotion detector")
    detector = EmotionDetector(api_url="http://localhost:8000")
    try:
        detector.run_continuous_detection(update_interval=1.0)
    except Exception as e:
        logger.error(f"Error in emotion detector: {e}")

if __name__ == "__main__":
    try:
        # Start backend in a separate thread
        backend_thread = threading.Thread(target=run_backend)
        backend_thread.daemon = True
        backend_thread.start()
        
        # Give the backend a moment to start
        time.sleep(2)
        
        # Start emotion detector in the main thread
        run_emotion_detector()
    except KeyboardInterrupt:
        logger.info("Shutting down NeuroMaze services...")
    except Exception as e:
        logger.error(f"Error in main: {e}") 