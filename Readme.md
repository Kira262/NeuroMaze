# 🧠 NeuroMaze: Adaptive Puzzleverse 🎮

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" alt="Python"/>
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/PyTorch-ML-orange?logo=pytorch" alt="PyTorch"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="MIT License"/>
  <img src="https://img.shields.io/badge/Made with-❤-maroon" alt="Made with Love">
</p>

---
> **NeuroMaze** is an AI-powered puzzle game that adapts itself in real-time based on your emotional state and playstyle. Combining game design, AI, and emotion detection, it delivers a truly personalized gameplay experience.

---

## ✨ Features

- 🤖 **Real-Time Emotion Detection** — Uses your webcam to sense stress, confusion, or excitement.
- 🧩 **Dynamic Puzzle Generation** — Mazes and puzzles evolve in complexity as you play.
- 🧠 **Player Behavior Profiling** — Learns your style: solver, explorer, rusher, tinkerer.
- 🗣️ **AI-Powered Game Narrator** — The in-game voice adapts its tone to your behavior and emotions.
- 🌐 **WebGL-Ready** — Playable in browser for demo and portfolio.

---

## 🚀 Quickstart

```bash
# 1. Clone the repo
$ git clone https://github.com/ira262/NeuroMaze.git
$ cd NeuroMaze

# 2. Install dependencies
$ pip install -r requirements.txt

# 3. Start the backend (FastAPI)
$ cd ai-backend
$ uvicorn main:app --reload

# 4. Run the emotion detector
$ cd ../emotion_detector
$ python detect_emotion.py

# 5. Start the game (Pygame)
$ cd ../game
$ python game.py
```

---

## 🛠️ Technologies Used

| Area              | Stack / Tools                                       |
| ----------------- | --------------------------------------------------- |
| Game Engine       | Pygame (Python)                                     |
| Emotion Detection | Python, OpenCV, MediaPipe, PyTorch CNN              |
| Backend API       | FastAPI, Uvicorn                                    |
| AI Models         | PyTorch (Emotion Classification, Behavior Modeling) |
| Communication     | REST (requests)                                     |
| Hosting           | (Planned) WebGL, Render/Vercel                      |

---

## 🧩 How It Works

```
[Webcam] → [Emotion Detector] → [AI Backend] → [Game Difficulty & Feedback]
      |             |                  |                  |
      |             |                  |                  |
      +---[Face]    +---[Emotion]      +---[Difficulty]   +---[Adaptive Maze]
```

---

## 📸 Screenshots / Demo

> _Coming soon!_

---

## 📦 Project Structure

```
NeuroMaze/
├── ai-backend/         # FastAPI backend for difficulty logic
├── emotion_detector/   # Real-time emotion detection
├── game/               # Pygame-based maze game
├── assets/             # Art, audio, and UI assets
├── demo/               # WebGL build or gameplay footage
├── requirements.txt    # Python dependencies
└── Readme.md           # This file
```

---

## 🧠 Roadmap

- [x] Basic Maze Navigation
- [x] Emotion Detector Integration
- [x] Backend AI Logic
- [ ] Puzzle Room Template
- [ ] Unity ↔ API Integration
- [ ] WebGL Build & Deployment

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

---

## 👤 Author

**Paavan**  
CSE Student | Full-stack Dev | AI Explorer  
[Portfolio](https://github.com/ira262)

---

## 📜 License

MIT License – Feel free to fork, remix, and build on top of this.
