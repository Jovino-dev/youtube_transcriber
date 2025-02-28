import yt_dlp
import whisper
import os
import sys
import ffmpeg

import shutil

# Directorios
OUTPUT_DIR = "output"
TEXT_DIR = "transcripts"
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(TEXT_DIR, exist_ok=True)

def download_audio(youtube_url):
    """Download the audio from a YouTube video using yt-dlp."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{OUTPUT_DIR}/audio.%(ext)s',
        'quiet': True
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_url, download=True)
        audio_path = os.path.join(OUTPUT_DIR, f"audio.{info_dict['ext']}")
        video_title = info_dict['title']
        
    return audio_path, video_title

def convert_to_wav(input_path):
    """Convert the audio file to WAV format using ffmpeg."""
    wav_path = os.path.join(OUTPUT_DIR, "audio.wav")
    ffmpeg.input(input_path).output(wav_path).run(overwrite_output=True)

    """.input(input_path)
    .output(wav_path, ac=1, ar=16000, format='wav')
    .run(overwrite_output=True, quiet=True)"""
    return wav_path

def transcribe_audio(audio_path, video_title):
    """Transcribe the audio file using the Whisper model."""
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    transcript_path = os.path.join(TEXT_DIR, f"{video_title}.txt")
    
    """Write the transcription to a text file, overwrite."""
    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(result["text"])
    
    print(f"\n✅ Transcription completed. Saved in: {transcript_path}")
    return transcript_path

def clean_output():
    """ Remove the output directory and create a new one."""
    shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

if __name__ == "__main__":
    youtube_url = sys.argv[1] if len(sys.argv) > 1 else input("📺 Input the YouTube URL: ")
    audio_file, video_title = download_audio(youtube_url)
    wav_file = convert_to_wav(audio_file)
    transcribe_audio(wav_file, video_title)
    clean_output()