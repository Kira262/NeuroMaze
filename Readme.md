# 🧠 NeuroMaze: Adaptive Puzzleverse 🎮

> **⚠ Disclaimer**  
> _This project is currently a prototype and may not function correctly._  
> _It is a work in progress and is intended for **experimental** and **demonstration** purposes only._  

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" alt="Python"/>
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/PyTorch-ML-orange?logo=pytorch" alt="PyTorch"/>
  <img src="https://img.shields.io/badge/Unity-Game-blue?logo=unity" alt="Unity"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="MIT License"/>
  <img src="https://img.shields.io/badge/Made with-❤-maroon" alt="Made with Love">
  <img src="https://img.shields.io/badge/Status-Alpha-orange" alt="Development Status">
</p>

> **NeuroMaze** is an AI-powered puzzle game that adapts itself in real-time based on your emotional state and playstyle. Combining Unity game design, AI, and emotion detection, it delivers a truly personalized gameplay experience.

## ✨ Features

- 🤖 **Real-Time Emotion Detection** — Uses your webcam to sense stress, confusion, or excitement
- 🧩 **Dynamic Puzzle Generation** — Mazes and puzzles evolve in complexity as you play
- 🧠 **Player Behavior Profiling** — Learns your style: solver, explorer, rusher, tinkerer
- 🗣️ **AI-Powered Game Narrator** — The in-game voice adapts its tone to your behavior and emotions
- 🌐 **Unity-Based Game** — High-quality 3D experience with WebGL export capability

## 🚀 Quickstart

### Prerequisites
- Windows 10/11
- Python 3.10 or higher
- Webcam
- Git (optional, for cloning)

### Installation Options

#### Option 1: One-Click Launch (Recommended)
1. Download the latest release
2. Run `main.py`
   - This will automatically:
     - Set up the Python environment
     - Install dependencies
     - Start the AI backend
     - Launch the game

#### Option 2: Manual Setup
```bash
# 1. Clone the repository
git clone https://github.com/Kira262/NeuroMaze.git
cd NeuroMaze

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the backend
python ai_backend/main.py

# 4. Launch the game
python main.py
```

### Configuration
The game automatically detects and configures settings based on your system, but you can manually adjust parameters as needed:

```python
# Sample configuration
config = {
    "backend": {
        "host": "127.0.0.1",
        "port": 8000
    },
    "emotion_detector": {
        "update_interval": 1.0,  # How often to check emotions (in seconds)
        "model": "emotion_detector/models/emotion_model.pth"
    },
    "game": {
        "default_difficulty": "Normal",
        "enable_emotion_detection": True
    }
}
```

## 🛠️ Development

### Project Structure
```
NeuroMaze/
├── main.py                  # Main application entry point
├── ai_backend/              # FastAPI backend for game logic
│   └── main.py              # Backend server
├── emotion_detector/        # Real-time emotion detection
│   ├── __init__.py
│   ├── backend_client.py    # Client for communicating with backend
│   ├── detect_emotion.py    # Emotion detection implementation
│   ├── emotion_detector.py  # Core detector class
│   ├── emotion_model.py     # PyTorch model definitions
│   └── models/              # Pre-trained emotion models
│       ├── emotion_album_model.pt
│       ├── emotion_model.pth
│       └── train_model.py   # Script for training custom models
├── assets/                  # Art, audio, and UI assets
├── demo/                    # Demo builds and gameplay footage
├── requirements.txt         # Python dependencies
├── checkgpu.py              # Utility to verify GPU availability
└── unity-game/              # Unity game project
    ├── Assets/              # Unity game assets
    │   ├── Scenes/          # Game scenes/levels
    │   ├── Scripts/         # C# game scripts
    │   ├── Settings/        # Unity project settings
    │   └── Sprites/         # 2D graphics
    └── ProjectSettings/     # Unity configuration
```

### Unity Integration
The project uses Unity as the game engine, with Python-based backend services for:
- Emotion detection through webcam
- AI-driven difficulty adjustment
- Dynamic maze generation

The Unity game communicates with the Python backend via REST API calls.

### Development Workflow
1. Start the AI backend: `python ai_backend/main.py`
2. Run emotion detection tests: `python emotion_detector/detect_emotion.py --test`
3. Open the Unity project in Unity Editor for game development
4. For full experience testing, run `python main.py`

## 🧠 How It Works

### System Architecture
```
[Webcam] → [Emotion Detector] → [AI Backend] → [Unity Game]
      |             |                  |                |
      |             |                  |                |
      +---[Face]    +---[Emotion]      +---[Difficulty] +---[Adaptive Maze]
```

### Emotion Detection
The system uses a PyTorch-based neural network trained on facial expressions to detect seven core emotions:
- Happiness
- Anger
- Fear
- Sadness
- Surprise
- Disgust
- Neutral

These emotions are processed in real-time and sent to the AI backend for game adaptation.

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

## 🆘 Troubleshooting

### Common Issues

1. **Webcam Not Working**
   - Check if webcam is properly connected
   - Verify camera permissions in Windows Settings
   - Try running: `python emotion_detector/detect_emotion.py --test-camera`

2. **GPU Acceleration Issues**
   - Run `python checkgpu.py` to verify GPU detection
   - Update your graphics drivers
   - Ensure PyTorch is installed with CUDA support if using NVIDIA GPU

3. **Backend Connection Issues**
   - Check if backend is running: `curl http://localhost:8000/health`
   - Verify port 8000 is available
   - Check for error messages in the console

4. **Unity Game Not Starting**
   - Verify Unity installation
   - Check for error logs in the console
   - Try running the standalone build if available

### Dependencies
Key dependencies include:
- PyTorch (ML framework)
- OpenCV (Computer vision)
- FastAPI (Backend server)
- MediaPipe (Face detection)
- TensorFlow (Additional ML capabilities)

Run `pip install -r requirements.txt` to install all dependencies.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## 📜 License

MIT License – Feel free to fork, remix, and build on top of this.

## 👤 Author

**Paavan**  
CSE Student | Full-stack Dev | AI Explorer  
[Portfolio](https://github.com/Kira262)

## 🙏 Acknowledgments

- MediaPipe for facial landmark detection
- PyTorch for the emotion recognition model
- FastAPI for the backend server
- Unity for the game engine

