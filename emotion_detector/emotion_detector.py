# emotion_detector.py
"""
EmotionDetector class for face detection and emotion prediction.
"""
import cv2
import mediapipe as mp
from torchvision import transforms
from PIL import Image
import numpy as np
from .emotion_model import EmotionCNN
import torch

class EmotionDetector:
    def __init__(self, model_path="./models/emotion_model.pth"):
        self.model = EmotionCNN()
        self.model.load_state_dict(torch.load(model_path, map_location=torch.device("cpu")))
        self.model.eval()
        self.transform = transforms.Compose([
            transforms.Resize((48, 48)),
            transforms.Grayscale(num_output_channels=1),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5], std=[0.5]),
        ])
        self.emotions = [
            "Anger", "Disgust", "Fear", "Happiness", "Sadness", "Surprise", "Neutral"
        ]
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(min_detection_confidence=0.5)

    def detect_emotion(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.face_mesh.process(rgb_frame)
        if result.multi_face_landmarks:
            for face_landmarks in result.multi_face_landmarks:
                h, w, _ = frame.shape
                face_region = self.extract_face_roi(face_landmarks, w, h, frame)
                if face_region is not None:
                    face_image = Image.fromarray(face_region)
                    input_tensor = self.transform(face_image).unsqueeze(0)
                    with torch.no_grad():
                        output = self.model(input_tensor)
                        _, predicted = torch.max(output, 1)
                        return self.emotions[predicted.item()]
        return "Neutral"

    def extract_face_roi(self, landmarks, width, height, frame):
        face_points = [
            (int(landmark.x * width), int(landmark.y * height))
            for landmark in landmarks.landmark
        ]
        x_min = max(min(face_points, key=lambda x: x[0])[0], 0)
        x_max = min(max(face_points, key=lambda x: x[0])[0], width)
        y_min = max(min(face_points, key=lambda x: x[1])[1], 0)
        y_max = min(max(face_points, key=lambda x: x[1])[1], height)
        if x_max <= x_min or y_max <= y_min:
            return None
        roi = frame[y_min:y_max, x_min:x_max]
        if roi.size == 0:
            return None
        return cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
