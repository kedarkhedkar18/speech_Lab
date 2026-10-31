
import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

SAMPLE_RATE = 16000
DURATION = 6

print("Loading speech recognition model...")
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

input("Press Enter, then speak for 6 seconds...")

print("Listening...")
audio = sd.rec(
    int(DURATION * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype="int16"
)
sd.wait()

write("recording.wav", SAMPLE_RATE, audio)

print("Transcribing...")
segments, info = model.transcribe(
    "recording.wav",
    beam_size=5
)

transcript = " ".join(
    segment.text.strip() for segment in segments
).strip()

print("Detected language:", info.language)
print("You said:", transcript)
