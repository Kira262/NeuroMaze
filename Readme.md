# 🧠 NeuroMaze: Adaptive Puzzleverse 🎮

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" alt="Python"/>
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/PyTorch-ML-orange?logo=pytorch" alt="PyTorch"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="MIT License"/>
  <img src="https://img.shields.io/badge/Made with-❤-maroon" alt="Made with Love">
  <img src="https://img.shields.io/badge/Status-Alpha-orange" alt="Development Status">
</p>

> **NeuroMaze** is an AI-powered puzzle game that adapts itself in real-time based on your emotional state and playstyle. Combining game design, AI, and emotion detection, it delivers a truly personalized gameplay experience.

## ✨ Features

- 🤖 **Real-Time Emotion Detection** — Uses your webcam to sense stress, confusion, or excitement
- 🧩 **Dynamic Puzzle Generation** — Mazes and puzzles evolve in complexity as you play
- 🧠 **Player Behavior Profiling** — Learns your style: solver, explorer, rusher, tinkerer
- 🗣️ **AI-Powered Game Narrator** — The in-game voice adapts its tone to your behavior and emotions
- 🌐 **WebGL-Ready** — Playable in browser for demo and portfolio

## 📸 Demo

> _Coming soon! We're working on a gameplay demo video to showcase NeuroMaze's adaptive features._

## 🚀 Quickstart

```bash
# 1. Clone the repo
git clone https://github.com/Kira262/NeuroMaze.git
cd NeuroMaze

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the backend (FastAPI)
cd ai-backend
uvicorn main:app --reload

# 4. Run the emotion detector
cd ../emotion_detector
python detect_emotion.py

# 5. Start the game (Pygame)
cd ../game
python game.py
```

## 🛠️ Tech Stack

| Area              | Technologies                                      |
|-------------------|--------------------------------------------------|
| Game Engine       | Pygame (Python)                                  |
| Emotion Detection | OpenCV, MediaPipe, PyTorch CNN                   |
| Backend API       | FastAPI, Uvicorn                                 |
| AI Models         | PyTorch (Emotion Classification, Behavior Modeling) |
| Communication     | REST API                                         |
| Hosting           | (Planned) WebGL, Render/Vercel                   |

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

## 🧠 How It Works

### System Architecture
```
[Webcam] → [Emotion Detector] → [AI Backend] → [Game Difficulty & Feedback]
      |             |                  |                  |
      |             |                  |                  |
      +---[Face]    +---[Emotion]      +---[Difficulty]   +---[Adaptive Maze]
```

### Difficulty Levels

| Emotion    | Difficulty | Game Adjustments                          |
|------------|------------|-------------------------------------------|
| Happiness  | Easy       | Slower enemies, more health, longer time  |
| Anger      | Hard       | Faster enemies, less health, shorter time |
| Fear       | Easy       | Reduced challenge to ease tension         |
| Sadness    | Easy       | Reduced challenge to improve mood         |
| Surprise   | Normal     | Standard game parameters                  |
| Disgust    | Hard       | Increased challenge                       |
| Neutral    | Normal     | Standard game parameters                  |

## 🧩 Roadmap

- [x] Basic Maze Navigation
- [x] Emotion Detector Integration
- [x] Backend AI Logic
- [ ] Puzzle Room Template
- [ ] Unity ↔ API Integration
- [ ] WebGL Build & Deployment

## 🛠️ Prerequisites

- Python 3.8+
- Virtual environment (recommended)
- Webcam access
- Unity 2021.3+ (for future Unity integration)

## 🤝 Contributing

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## 💬 Getting Help

Having trouble? Here are some common solutions:

1. **Webcam Issues**
   - Ensure your webcam is properly connected and accessible
   - Check camera permissions in your system settings
   - Try a different camera if available

2. **Installation Problems**
   - Make sure you're using Python 3.8 or higher
   - Create a fresh virtual environment
   - Check the [issues page](https://github.com/Kira262/NeuroMaze/issues) for known problems

3. **Emotion Detection**
   - Ensure good lighting conditions
   - Position yourself properly in front of the camera
   - Check if the emotion model is properly loaded

For more help, please [open an issue](https://github.com/Kira262/NeuroMaze/issues/new) or join our community!

## 👤 Author

**Paavan**  
CSE Student | Full-stack Dev | AI Explorer  
[Portfolio](https://github.com/Kira262)

## 📜 License

MIT License – Feel free to fork, remix, and build on top of this.

## 🙏 Acknowledgments

- MediaPipe for facial landmark detection
- PyTorch for the emotion recognition model
- FastAPI for the backend server
- Unity for the game engine
