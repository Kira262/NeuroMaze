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

## System Overview

NeuroMaze consists of three main components:
1. **Emotion Detector**: Python-based facial expression recognition
2. **AI Backend**: FastAPI server that processes emotions and determines difficulty
3. **Unity Game**: Adaptive puzzle game that responds to player emotions

## Prerequisites

### Python Environment
- Python 3.8 or higher
- Virtual environment (recommended)

### Unity
- Unity 2021.3 or higher
- TextMeshPro package

## Installation

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/NeuroMaze.git
cd NeuroMaze
```

2. **Set up Python environment**:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. **Download the emotion model**:
- Place the emotion detection model in `models/emotion_model.pth`
- If you don't have a model, you can train one using the provided training scripts

## Running the System

### 1. Start the AI Services

Open a terminal and run:
```bash
python main.py
```
This will start:
- The emotion detector on port 8001
- The backend server on port 8000

### 2. Set up the Unity Project

1. Open the Unity project in `unity-game/`
2. Import TextMeshPro if not already installed
3. Set up the scene:
   - Create a new scene or use the provided sample scene
   - Add the following GameObjects:
     - GameManager (empty GameObject with GameManager script)
     - DifficultyManager (empty GameObject with DifficultyManager script)
     - Player (3D object with PlayerController script)
     - Canvas with EmotionUI components

### 3. Configure the Scene

1. **Player Setup**:
   - Add a Rigidbody component
   - Configure constraints (freeze rotation on X and Z)
   - Set appropriate drag values

2. **UI Setup**:
   - Create a Canvas
   - Add EmotionPanel with:
     - EmotionText (TextMeshPro)
     - DifficultyText (TextMeshPro)
     - FeedbackText (TextMeshPro)
     - EmotionIcon (Image)
   - Add emotion icons to the Assets/Sprites/Emotions folder

3. **Camera Setup**:
   - Position the camera to view the player
   - Adjust field of view as needed

## How It Works

### Emotion Detection Flow
1. The emotion detector captures webcam footage
2. Facial expressions are analyzed in real-time
3. Detected emotions are sent to the backend
4. The backend processes the emotion and determines difficulty
5. The Unity game receives the difficulty setting
6. Game parameters are adjusted accordingly

### Difficulty Levels

The game adjusts based on detected emotions:

| Emotion    | Difficulty | Game Adjustments                          |
|------------|------------|-------------------------------------------|
| Happiness  | Easy       | Slower enemies, more health, longer time  |
| Anger      | Hard       | Faster enemies, less health, shorter time |
| Fear       | Easy       | Reduced challenge to ease tension         |
| Sadness    | Easy       | Reduced challenge to improve mood         |
| Surprise   | Normal     | Standard game parameters                  |
| Disgust    | Hard       | Increased challenge                       |
| Neutral    | Normal     | Standard game parameters                  |

### Game Parameters

The following parameters are adjusted based on difficulty:

- Enemy Speed
- Enemy Spawn Rate
- Player Health
- Player Speed
- Puzzle Time Limit

## Testing

1. **Start the AI Services**:
```bash
python main.py
```

2. **Run the Unity Game**:
- Press Play in the Unity Editor
- Make sure your webcam is accessible
- Test different facial expressions to see the difficulty adjust

3. **Verify the System**:
- Check the Unity Console for any errors
- Monitor the Python terminal for emotion detection output
- Verify that the UI updates with current emotion and difficulty

## Troubleshooting

### Common Issues

1. **Webcam Not Detected**:
   - Check if the webcam is properly connected
   - Verify camera permissions
   - Try a different camera if available

2. **Connection Errors**:
   - Ensure the backend is running on port 8000
   - Check if the Unity game is using the correct backend URL
   - Verify network connectivity

3. **Emotion Detection Issues**:
   - Ensure good lighting conditions
   - Position yourself properly in front of the camera
   - Check if the emotion model is properly loaded

### Debugging

1. **Unity Console**:
   - Monitor for any error messages
   - Check if difficulty updates are being received

2. **Python Terminal**:
   - Look for emotion detection output
   - Check for any backend errors

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- MediaPipe for facial landmark detection
- PyTorch for the emotion recognition model
- FastAPI for the backend server
- Unity for the game engine
