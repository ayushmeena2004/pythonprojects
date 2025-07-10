import pyaudio as pd
import wave

# Audio settings
FORMAT = pd.paInt16  # 16-bit audio format
CHANNELS = 1  # Mono audio
RATE = 44100  # Sample rate (Hz)
CHUNK = 1024  # Buffer size
RECORD_SECONDS = 5  # Recording duration
OUTPUT_FILE = "output.wav"  # File to save recording

# Initialize PyAudio
audio = pd.PyAudio()

# Open stream for recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Recording...")

frames = []

# Capture audio data
for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Recording finished.")

# Stop and close the stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recording as a WAV file
with wave.open(OUTPUT_FILE, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

print(f"Audio saved as {OUTPUT_FILE}")

# Playback the recorded audio
def play_audio(file):
    wf = wave.open(file, 'rb')
    audio = pd.PyAudio()
    
    stream = audio.open(format=audio.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
    
    data = wf.readframes(CHUNK)
    
    while data:
        stream.write(data)
        data = wf.readframes(CHUNK)
    
    stream.stop_stream()
    stream.close()
    audio.terminate()

print("Playing recorded audio...")
play_audio(OUTPUT_FILE)
print("Playback finished.")
