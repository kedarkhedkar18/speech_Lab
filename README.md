# speech_Lab

A beginner-friendly Python voice assistant prototype inspired by AI-powered speech Recognition

## Features
- Captures voice input through a microphone.
- Converts speech into text using Google Speech Recognition.
- Generates responses using the Qwen 2.5 model through Ollama.
- Speaks responses using Microsoft Edge Text-to-Speech.
- Saves notes to a local text file when requested.

## Tech Stack
- Python
- Ollama
- Qwen 2.5 (1.5B)
- SpeechRecognition
- Requests
- Edge TTS

## How It Works

1. The microphone captures the user's speech.
2. Speech Recognition converts audio into text.
3. The text is sent to the locally running Ollama model.
4. Python processes the response and handles note-saving requests.
5. Edge TTS converts the response into speech.

## Setup

1. Install Python and [Ollama](https://ollama.com/).
2. Download the model:

   ```bash
   ollama pull qwen2.5:1.5b
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start Ollama and run:

   ```bash
   python voice_assistant.py
   ```

## Note
This is an experimental voice-assistant prototype. It runs on a computer 
