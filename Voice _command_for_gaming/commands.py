import pyautogui

def execute_command(command):
    actions = {
        "jump": lambda: pyautogui.press("space"),
        "shoot": lambda: pyautogui.click(),
        "run": lambda: pyautogui.keyDown("shift"),
        "stop": lambda: pyautogui.keyUp("shift"),
        "left": lambda: pyautogui.press("a"),
        "right": lambda: pyautogui.press("d"),
        "forward": lambda: pyautogui.press("w"),
        "backward": lambda: pyautogui.press("s"),
    }

    action = actions.get(command)
    if action:
        print(f"Executing: {command}")
        action()
    else:
        print("Unknown command.")
