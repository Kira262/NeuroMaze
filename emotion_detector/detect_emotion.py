import cv2
import mediapipe as mp
import torch
from torchvision import transforms
from PIL import Image
import time
import sys
import os

# Handle imports properly whether run as script or module
try:
    # Try direct import first (when running directly)
    from emotion_model import EmotionCNN
    from backend_client import send_emotion_data
except ImportError:
    # Fall back to package import (when imported as module)
    from emotion_detector.emotion_model import EmotionCNN
    from emotion_detector.backend_client import send_emotion_data


class EmotionDetector:
    def __init__(self):
        self.model = EmotionCNN()
        # Fix model path for both direct and package imports
        try:
            # Try local path first (when running from emotion_detector directory)
            model_path = "./models/emotion_model.pth"
            self.model.load_state_dict(torch.load(model_path, map_location="cpu"))
        except FileNotFoundError:
            # Fall back to package path (when imported as module)
            model_path = "./emotion_detector/models/emotion_model.pth"
            self.model.load_state_dict(torch.load(model_path, map_location="cpu"))

        self.model.eval()

        self.transform = transforms.Compose(
            [
                transforms.Resize((48, 48)),
                transforms.Grayscale(num_output_channels=1),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.5], std=[0.5]),
            ]
        )

        self.emotions = [
            "Anger",
            "Disgust",
            "Fear",
            "Happiness",
            "Sadness",
            "Surprise",
            "Neutral",
        ]

        # Initialize MediaPipe FaceMesh
        self.mp_face_mesh = mp.solutions.face_mesh  # type: ignore
        self.face_mesh = self.mp_face_mesh.FaceMesh(min_detection_confidence=0.5)

    def detect_emotion(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.face_mesh.process(rgb_frame)

        # Check if face landmarks were detected
        if result.multi_face_landmarks:
            for face_landmarks in result.multi_face_landmarks:
                h, w, _ = frame.shape
                # Extract face landmarks as x,y coordinates
                landmarks_x = [int(lm.x * w) for lm in face_landmarks.landmark]
                landmarks_y = [int(lm.y * h) for lm in face_landmarks.landmark]

                # Calculate bounding box
                x_min = max(0, min(landmarks_x))
                y_min = max(0, min(landmarks_y))
                x_max = min(w, max(landmarks_x))
                y_max = min(h, max(landmarks_y))

                # Extract face region
                if x_min < x_max and y_min < y_max:
                    face_roi = frame[y_min:y_max, x_min:x_max]
                    if face_roi.size == 0:
                        continue

                    # Convert to RGB for PIL
                    face_image = Image.fromarray(
                        cv2.cvtColor(face_roi, cv2.COLOR_BGR2RGB)
                    )

                    # Apply transformations for the model
                    input_tensor = self.transform(face_image)
                    # Add batch dimension
                    input_tensor = input_tensor.unsqueeze(0)  # type: ignore

                    with torch.no_grad():
                        output = self.model(input_tensor)
                        _, predicted = torch.max(output, 1)
                        # Use the predicted index to get emotion name
                        emotion_index = predicted.item()
                        if 0 <= emotion_index < len(self.emotions):
                            return self.emotions[emotion_index]  # type: ignore

        return "Neutral"


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    detector = EmotionDetector()

    last_call = time.time()
    feedback = "Waiting for analysis..."
    difficulty = "Normal"

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            emotion = detector.detect_emotion(frame)

            # Send to backend every 3 seconds
            if time.time() - last_call > 3:
                # simulate game metrics here (or pull real ones later)
                puzzle_time = 55.0
                error_rate = 0.25

                result = send_emotion_data(emotion, puzzle_time, error_rate)
                if result:
                    difficulty = result.get("difficulty", difficulty)
                    feedback = result.get("feedback", feedback)
                    # simulate game metrics here (or pull real ones later)
                    puzzle_time = 55.0
                    error_rate = 0.25

            # Display results
            cv2.putText(
                frame,
                f"Emotion: {emotion}",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
            )
            cv2.putText(
                frame,
                f"Difficulty: {difficulty}",
                (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
            )
            cv2.putText(
                frame,
                f"Feedback: {feedback}",
                (10, 110),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2,
            )

            cv2.imshow("Emotion Detection", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        cap.release()
        cv2.destroyAllWindows()
