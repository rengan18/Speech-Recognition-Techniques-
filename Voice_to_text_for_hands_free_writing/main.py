import speech_recognition as sr
import datetime

def write_to_file(text):
    filename = "voice_notes.txt"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {text}\n")
    print(f"Saved: {text}")

def voice_to_text():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Voice to Text: Start speaking. Say 'stop writing' to finish.")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)

        while True:
            print("Listening...")
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio).lower()
                print(f"You said: {text}")

                if "stop writing" in text:
                    print("Stopping dictation.")
                    break

                write_to_file(text)

            except sr.UnknownValueError:
                print("Sorry, I didn’t catch that.")
            except sr.RequestError:
                print("Network error or API not available.")

if __name__ == "__main__":
    voice_to_text()
