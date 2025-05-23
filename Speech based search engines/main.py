import speech_recognition as sr
import webbrowser

def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Say something...")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError:
        print("Could not request results; check your internet connection.")
    return None

def search_web(query):
    if query:
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        print(f"Searching for: {query}")

if __name__ == "__main__":
    spoken_text = recognize_speech()
    search_web(spoken_text)
