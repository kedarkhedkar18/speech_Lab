
import asyncio
import edge_tts
import os
import time
import requests
import speech_recognition as sr
import pyttsx3

from app import run_assistant


# ---------------- CONFIGURATION ----------------

LANGUAGE = "en-IN"
RECORD_SECONDS = 7
SPEECH_RATE = 145

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8

# Initialize text-to-speech once and reuse it.
def initialize_speaker():
    engine = pyttsx3.init()
    engine.setProperty("rate", SPEECH_RATE)
    engine.setProperty("volume", 1.0)
    return engine

speaker = initialize_speaker()


# ---------------- TEXT TO SPEECH ----------------




def speak(text):
    print("\nAssistant:", text)

    async def generate_audio():
        filename = "assistant_reply.mp3"

        communicate = edge_tts.Communicate(
            str(text),
            voice="en-IN-NeerjaNeural"
        )

        await communicate.save(filename)

        os.startfile(filename)

        # Give Windows time to finish playing the audio.
        # This is a temporary approach; we'll improve it if needed.
        time.sleep(max(3, len(str(text)) * 0.12))

    asyncio.run(generate_audio())




# ---------------- SPEECH TO TEXT ----------------

def listen():
    """Record speech and convert it into text."""
    with sr.Microphone() as source:
        print("\nListening... Speak clearly.")
        audio = recognizer.record(
            source,
            duration=RECORD_SECONDS
        )

    print("Converting speech to text...")

    question = recognizer.recognize_google(
        audio,
        language=LANGUAGE
    ).strip()

    print("You:", question)
    return question


# ---------------- MAIN ASSISTANT LOOP ----------------

def main():
    print("=" * 42)
    print("       AI GLASSES VOICE ASSISTANT")
    print("=" * 42)
    print("Press Enter to speak.")
    print("Say 'exit' to quit.\n")

    while True:
        try:
            input("Press Enter when you're ready to speak...")

            question = listen()

            if question.lower().strip(" .,!?'\"") in {
                "exit", "quit", "stop"
            }:
                speak("Goodbye! See you soon.")
                break

            if not question:
                print("No speech detected. Please try again.")
                continue

            print("Thinking...")
            answer = run_assistant(question)

            # Print and speak each response.
            speak(answer)

        except sr.UnknownValueError:
            print("I couldn't understand that. Please speak clearly.")

        except sr.RequestError as error:
            print("Speech recognition service error:", error)
            print("Check your internet connection.")

        except requests.RequestException as error:
            print("Ollama connection error:", error)
            print("Check that Ollama is running, then try again.")

        except OSError as error:
            print("Microphone or audio device error:", error)
            print("Check your microphone and speakers.")

        except KeyboardInterrupt:
            print("\nAssistant stopped.")
            break

        except Exception as error:
            print("Unexpected error:", error)

    # Release the speech engine when exiting.
    try:
        speaker.stop()
    except Exception:
        pass


if __name__ == "__main__":
    main()
