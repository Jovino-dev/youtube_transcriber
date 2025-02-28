# 🎤 YouTube Audio Transcriber

This script allows you to download the audio from a **YouTube** video and transcribe it using **OpenAI Whisper**.

## 🚀 Features
👉 Automatically downloads the audio from a YouTube video.
👉 Converts the audio to WAV format.
👉 Uses **Whisper** to transcribe the audio content.
👉 Saves the transcription in a text file.
👉 Supports execution with **arguments** or **interactive mode**.

## 🛠️ Installation and Setup

### **1️⃣ Clone the repository**
```bash
git clone https://github.com/TU_USUARIO/youtube_transcriber.git
cd youtube_transcriber
```
### **2️⃣ Create .venv and Install dependencies**

To create the environment with venv, run:
```bash
python -m venv .venv
```

Activate the environment:
- **Windows:**
  ```bash
  .venv\Scripts\activate
  ```
- **Linux/MacOS:**
  ```bash

Make sure you have **Python 3.8+** installed and run:
```bash
pip install -r requirements.txt
```

After installing the dependencies, you can deactivate the environment with:
```bash
deactivate
```

### **3️⃣ Install FFmpeg (if not installed)**
- **Windows:** Download from [FFmpeg.org](https://ffmpeg.org/download.html) and add it to `PATH`.
- **Linux:**
  ```bash
  sudo apt update && sudo apt install ffmpeg
  ```
- **MacOS:**
  ```bash
  brew install ffmpeg
  ```

## 🎯 Script Usage

### **1️⃣ Interactive mode (without arguments)**

Activate the environment:

```bash
.venv\Scripts\activate
```

Run the script and enter the video URL when prompted:
```bash
python transcriber.py
```

Or pass the video URL directly when running the script:
```bash
python transcriber.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

After the transcription is complete, deactivate the environment:
```bash
deactivate
```

### **2️⃣ Automatic mode (with URL as an argument)**
Pass the video URL directly when running the script:
```bash
python transcriber.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

### **3️⃣ Transcription output location**
The transcribed text will be saved in:
```
transcriptions/VIDEO_TITLE.txt
```

## ⚙️ Optional: Update dependencies
If you need to update dependencies in the future, use:
```bash
pip freeze > requirements.txt
```

## 🛠️ Contribution and Development
1. **Fork the repository.**
2. Create a new branch:
   ```bash
   git checkout -b my-new-branch
   ```
3. Make changes and commit:
   ```bash
   git commit -m "Added new feature"
   ```
4. Push changes and create a **Pull Request**.

## 📚 License
This project is distributed under the **MIT License**.