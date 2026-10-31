
import pyttsx3
import time

engine = pyttsx3.init()
engine.setProperty("rate", 145)
engine.setProperty("volume", 1.0)

for i in range(1, 4):
    print(f"Speaking message {i}...")
    engine.say(f"Message number {i}")
    engine.runAndWait()
    print(f"Message {i} finished.")
    time.sleep(2)

print("All tests completed.")
