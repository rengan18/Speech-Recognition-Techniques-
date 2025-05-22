import speech_recognition as sr
import webbrowser
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please speak your query.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
        return ""
    except sr.RequestError:
        print("Could not request results. Check your internet connection.")
        return ""

def search_web(query):
    if query:
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)
        speak(f"Searching Google for {query}")
    else:
        speak("No search query provided.")

if __name__ == "__main__":
    speak("Welcome to the speech-based search engine")
    query = take_command()
    search_web(query)
