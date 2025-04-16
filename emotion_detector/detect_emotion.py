import cv2
import torch
from PIL import Image
import numpy as np
import time
import os
import sys

from .emotion_detector import EmotionDetector
from .backend_client import send_to_backend

cap = cv2.VideoCapture(0)
emotion_detector = EmotionDetector()

last_call = time.time()
feedback = "Waiting for analysis..."
difficulty = "Normal"
bg_color = (0, 0, 0)


while True:
    ret, frame = cap.read()
    if not ret:
        break

    emotion = emotion_detector.detect_emotion(frame)

    # Send to backend every 3 seconds
    if time.time() - last_call > 3:
        result = send_to_backend(emotion)
        difficulty = result["difficulty"]
        feedback = result["feedback"]
        last_call = time.time()

        # Change color based on difficulty
        if difficulty == "Easy":
            bg_color = (0, 255, 0)
        elif difficulty == "Normal":
            bg_color = (255, 255, 0)
        elif difficulty == "Hard":
            bg_color = (0, 0, 255)

    # Overlay background rectangle
    overlay = frame.copy()
    cv2.rectangle(overlay, (10, 10), (620, 120), bg_color, -1)
    frame = cv2.addWeighted(overlay, 0.3, frame, 0.7, 0)

    # Display emotion + difficulty + feedback
    cv2.putText(
        frame,
        f"Emotion: {emotion}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2,
    )
    cv2.putText(
        frame,
        f"Difficulty: {difficulty}",
        (20, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2,
    )
    cv2.putText(
        frame,
        f"{feedback}",
        (20, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        1,
    )

    cv2.imshow("NeuroMaze: Emotion + AI Feedback", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
