# Sentairos AI 🦾✨

Sentairos AI is an open-source, desktop-based anime AI assistant and autonomous agent. It combines high-end anime aesthetics with powerful terminal capabilities, allowing you to interact with a virtual companion that can execute tasks directly on your machine.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Framework](https://img.shields.io/badge/framework-FastAPI%20%7C%20Tauri-orange.svg)

## 🌟 Features

- **Live2D Anime Avatar:** An interactive 2D companion that follows your mouse and reacts to your input.
- **Voice Synthesis:** Integrated Text-to-Speech (TTS) for a conversational experience.
- **Agentic Terminal:** Full shell access! Prefix your messages with `/sh` to run commands on your machine (e.g., `/sh ls -la`, `/sh mkdir project`).
- **Privacy Centric:** Saves your Gemini API key locally in an encrypted-style JSON config.
- **Native Desktop App:** Runs as a standalone OS window (not in a browser).

## 🛠️ Technical Stack

- **Frontend:** HTML5, Tailwind CSS, PixiJS, Live2D Cubism.
- **Backend:** Python, FastAPI, Pywebview (for native window rendering).
- **Zeka (Brain):** Google Gemini 1.5 Pro (Configurable via UI).
- **Execution:** Subprocess-based shell integration.

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- A Gemini API Key (get it from [Google AI Studio](https://aistudio.google.com/))

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/raprapyap1000-ux/sentairos-ai.git
   cd sentairos-ai
   ```

2. **Install dependencies:**
   ```bash
   pip install -r backend/requirements.txt
   ```

3. **Launch the application:**
   ```bash
   python launcher.py
   ```

4. **Configuration:**
   Click the **Gear icon** in the top right corner of the app to enter your API Key.

## 🤖 Usage

- **Chat:** Simply type a message to talk to Sentairos.
- **Execute Commands:** Type `/sh <your-command>` to let the agent perform tasks on your system.
- **Settings:** Manage your API keys and local preferences.

## 🗺️ Roadmap

- [ ] Support for local LLMs (Ollama/LM Studio).
- [ ] Advanced Voice Models (Piper/Bark) for realistic anime voices.
- [ ] File Master Skill: Automated file editing and searching.
- [ ] Widget Mode: Pin Sentairos to the corner of your screen.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to make Sentairos even better.

---
*Created with ❤️ by Nihat Aydın & Sentinel.*
