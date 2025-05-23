import speech_recognition as sr
from commands import execute_command

def listen_for_command():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Listening for gaming commands... (say 'exit' to quit)")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)

        while True:
            print("Say a command:")
            audio = recognizer.listen(source)

            try:
                command = recognizer.recognize_google(audio).lower()
                print(f"You said: {command}")
                
                if command == "exit":
                    print("Exiting voice command system.")
                    break

                execute_command(command)

            except sr.UnknownValueError:
                print("Sorry, I didn't catch that.")
            except sr.RequestError:
                print("Network error.")

if __name__ == "__main__":
    listen_for_command()
