
import speech_recognition as sr

recognizer = sr.Recognizer()

print("Voice AI Assistant - Speech-to-Text Test")

try:
    with sr.Microphone() as source:
        # Reduce background noise before recording
        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        # Wait until you are ready
        input("Press Enter when you're ready to speak...")

        print("Recording for 5 seconds. Speak now!")

        # Record your voice for 5 seconds
        audio = recognizer.record(
            source,
            duration=5
        )

    print("Recording finished. Recognising speech...")

    # Convert speech into text using Google's online service
    text = recognizer.recognize_google(
        audio,
        language="en-IN"
    )

    print("\nYou said:", text)

except sr.UnknownValueError:
    print("Sorry, I couldn't understand the speech.")

except sr.RequestError as error:
    print("Speech recognition service error:", error)

except Exception as error:
    print("Something went wrong:", error)
