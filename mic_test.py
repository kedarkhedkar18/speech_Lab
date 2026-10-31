
import sounddevice as sd
from scipy.io.wavfile import write

sample_rate = 16000
duration = 5

print("Available microphones:")
print(sd.query_devices())

input("Press Enter when ready to record...")

print("Recording for 5 seconds. Speak now!")

audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype="int16"
)

sd.wait()

write("mic_test.wav", sample_rate, audio)

print("Recording saved as mic_test.wav")
print("Now play the WAV file and check whether your voice is audible.")
