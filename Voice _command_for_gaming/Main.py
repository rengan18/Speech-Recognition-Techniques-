import speech_recognition as sr
import pyautogui
import time

# Define your voice commands and corresponding keyboard keys
commands = {
    "jump": "space",
    "move forward": "w",
    "move back": "s",
    "turn left": "a",
    "turn right": "d",
    "reload": "r",
    "crouch": "ctrl",
    "shoot": "left",
    "aim": "right"
}

def recognize_command():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Could not understand the command.")
    except sr.RequestError:
        print("Speech recognition service unavailable.")
    return None

def execute_command(command):
    for phrase, key in commands.items():
        if phrase in command:
            print(f"Executing: {phrase} -> {key}")
            if key in ["left", "right"]:  # mouse actions
                pyautogui.click(button=key)
            elif key == "ctrl":
                pyautogui.keyDown("ctrl")
                time.sleep(0.5)
                pyautogui.keyUp("ctrl")
            else:
                pyautogui.press(key)
            return
    print("Command not recognized.")

if __name__ == "__main__":
    while True:
        cmd = recognize_command()
        if cmd:
            execute_command(cmd)
