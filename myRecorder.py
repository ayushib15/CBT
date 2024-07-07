import sounddevice as sd
import wavio
10
def record_audio(duration, filename):
    # Record audio
    print("Recording...")
    audio = sd.rec(int(duration * 44100), samplerate=44100, channels=2, dtype='int16')
    sd.wait()

    # Save audio as WAV file
    wavio.write(filename, audio, 44100, sampwidth=2)

    print(f"Audio recorded and saved as {filename}")

if __name__ == "__main__":
    duration = int(input("Enter duration of recording (in seconds): "))
    filename = input("Enter filename to save recording (without extension): ") + ".wav"
    record_audio(duration, filename)