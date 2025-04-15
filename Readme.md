# 🧠 NeuroMaze: Adaptive Puzzleverse 🎮

**NeuroMaze** is an AI-powered puzzle game that adapts itself in real-time based on the player's emotional state and playstyle. Designed as a solo hackathon project, it combines game design, AI, and emotion detection to deliver a personalized gameplay experience.

---

## 🎯 What Makes It Unique?

- 🤖 **Emotion Detection via Webcam** — Uses real-time facial analysis to detect stress, confusion, or excitement.
- 🧩 **Dynamic Puzzle Generation** — Puzzles evolve in complexity based on how you're performing.
- 🧠 **Player Behavior Profiling** — Game learns your style: solver, explorer, rusher, tinkerer.
- 🗣️ **AI-Powered Game Narrator** — The in-game voice adapts its tone to your behavior and emotions.
- 🌐 **WebGL-Ready** — Fully playable in browser for demo and portfolio.

---

## 🛠️ Technologies Used

| Area              | Stack / Tools                                       |
| ----------------- | --------------------------------------------------- |
| Game Engine       | Unity 3D + C# + URP                                 |
| Emotion Detection | Python, OpenCV, MediaPipe, FER2013 CNN              |
| Backend API       | FastAPI, Uvicorn                                    |
| AI Models         | PyTorch (Emotion Classification, Behavior Modeling) |
| Communication     | UnityWebRequest (Unity) ↔ FastAPI (Python)          |
| Hosting           | GitHub Pages (WebGL), Render/Vercel (API)           |

---

## 🔍 Modules Breakdown

- `unity-game/`: Unity project with puzzle mechanics, player controller, API calls.
- `ai-backend/`: FastAPI backend serving difficulty levels and behavior analysis.
- `emotion-detector/`: Real-time webcam emotion detection using OpenCV.
- `assets/`: Textures, models, audio, and UI art.
- `demo/`: WebGL build or gameplay footage.

---

## 📸 Screenshots / Demo

_(Will add after development is complete)_

---

## 🧩 Puzzle Mechanic Overview

- Each room in the maze is a new logic challenge.
- Based on your frustration level (from face), puzzles will:
  - Reduce/increase complexity
  - Offer hints or get sarcastic
  - Alter environmental effects (color, light, sound)

---

## 🚧 Roadmap

- [ ] Basic Maze Navigation
- [ ] Puzzle Room Template
- [ ] Emotion Detector Integration
- [ ] Backend AI Logic
- [ ] Unity ↔ API Integration
- [ ] WebGL Build & Deployment

---

## 👤 Author

**Paavan**  
CSE Student | Full-stack Dev | AI Explorer  
[Portfolio Website]() _(Coming soon)_

---

## 📜 License

MIT License – Feel free to fork, remix, and build on top of this.
