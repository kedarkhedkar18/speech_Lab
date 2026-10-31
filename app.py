
import requests
from pathlib import Path

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "qwen2.5:1.5b"
NOTES_FILE = Path("notes.txt")


def save_note(note):
    """Save a note to a local text file."""
    with NOTES_FILE.open("a", encoding="utf-8") as file:
        file.write(note + "\n")

    return f"Note saved successfully: {note}"


def ask_ai(question):
    """Send a question to Ollama and return its response."""
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a concise AI glasses assistant. "
                        "Reply in 2 sentences or less. "
                        "Match the user's language. "
                        "If the user wants to save a note, "
                        "reply with SAVE_NOTE: followed by the note. "
                        "Do not use SAVE_NOTE for ordinary questions."
                    ),
                },
                {
                    "role": "user",
                    "content": question,
                },
            ],
            "stream": False,
        },
        timeout=300,
    )

    response.raise_for_status()
    return response.json()["message"]["content"].strip()


def run_assistant(question):
    """Answer a question or save a note when requested."""
    answer = ask_ai(question)

    if answer.startswith("SAVE_NOTE:"):
        note = answer.removeprefix("SAVE_NOTE:").strip()

        if note:
            return save_note(note)

    return answer


# Run the text-based assistant only when app.py is executed directly.
if __name__ == "__main__":
    print("AI Glasses Assistant ready!")
    print("Type 'exit' to quit.")

    while True:
        question = input("\nYou: ").strip()

        if question.lower() == "exit":
            print("Assistant: Bye, bro!")
            break

        if question:
            try:
                answer = run_assistant(question)
                print("\nAssistant:", answer)

            except requests.RequestException as error:
                print("Connection error:", error)
