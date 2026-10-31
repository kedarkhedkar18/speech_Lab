
import asyncio
import edge_tts
import os

async def main():
    messages = [
        "This is audio test number one.",
        "This is audio test number two.",
        "This is audio test number three."
    ]

    for i, message in enumerate(messages, start=1):
        print(f"Playing message {i}...")

        communicate = edge_tts.Communicate(
            message,
            voice="en-IN-NeerjaNeural"
        )

        filename = f"test_audio_{i}.mp3"
        await communicate.save(filename)

        os.startfile(filename)

        input("Press Enter after the audio finishes...")

    print("All three audio tests completed.")

asyncio.run(main())
