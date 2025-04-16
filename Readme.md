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

## 🚀 Quickstart

### Prerequisites
- Windows 10/11
- Python 3.8 or higher
- Webcam
- Git (optional, for cloning)

### Installation Options

#### Option 1: One-Click Launch (Recommended)
1. Download the latest release
2. Run `launch.bat`
   - This will automatically:
     - Set up the Python environment
     - Install dependencies
     - Start the backend
     - Launch the game

#### Option 2: Manual Setup
```bash
# 1. Clone the repository
git clone https://github.com/Kira262/NeuroMaze.git
cd NeuroMaze

# 2. Run setup script
setup.bat

# 3. Start the game
run_game.bat
```

### Configuration
Customize your experience by editing `config.json`:
```json
{
    "backend": {
        "host": "0.0.0.0",    // Change if running on a different machine
        "port": 8000          // Change if port 8000 is in use
    },
    "emotion_detector": {
        "update_interval": 1.0 // How often to check emotions (in seconds)
    },
    "game": {
        "default_difficulty": "Normal",
        "log_level": "INFO"   // Options: DEBUG, INFO, WARNING, ERROR
    }
}
```

## 🛠️ Development

### Project Structure
```
NeuroMaze/
├── ai-backend/         # FastAPI backend for difficulty logic
├── emotion_detector/   # Real-time emotion detection
├── game/               # Pygame-based maze game
├── assets/             # Art, audio, and UI assets
├── demo/               # WebGL build or gameplay footage
├── scripts/            # Utility scripts
│   ├── launch.bat      # One-click launcher
│   ├── setup.bat       # Environment setup with version checks
│   ├── run_game.bat    # Game runner
│   ├── cleanup.bat     # Environment cleanup
│   └── test_installation.bat  # Installation verification
├── requirements.txt    # Python dependencies
└── config.json         # Configuration file
```

### Available Scripts
- `launch.bat` - One-click setup and launch
- `setup.bat` - Set up Python environment with version checks
- `run_game.bat` - Start the game
- `cleanup.bat` - Reset environment
- `test_installation.bat` - Verify installation and dependencies

### Installation Verification
After setup, you can verify your installation by running:
```bash
test_installation.bat
```
This will check:
- Python environment
- Virtual environment
- Required packages
- Webcam access
- Backend health

### Development Workflow
1. Run `setup.bat` to create the environment
2. Use `test_installation.bat` to verify setup
3. Make your changes
4. Test with `run_game.bat`
5. Use `cleanup.bat` to reset if needed

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

## 🆘 Troubleshooting

### Common Issues

1. **Webcam Not Working**
   - Check if webcam is properly connected
   - Verify camera permissions in Windows Settings
   - Try a different USB port
   - Test with another application (e.g., Camera app)

2. **Backend Connection Issues**
   - Check if backend is running: `curl http://localhost:8000/health`
   - Verify port 8000 is available
   - Check firewall settings
   - Look for error messages in the console

3. **Installation Problems**
   - Run `cleanup.bat` and try again
   - Ensure Python 3.8+ is installed
   - Check if pip is up to date
   - Verify virtual environment creation

### Debugging Tools
- Check logs in the console
- Use the health endpoint: `http://localhost:8000/health`
- Monitor emotion detection in real-time
- Check game difficulty adjustments

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

