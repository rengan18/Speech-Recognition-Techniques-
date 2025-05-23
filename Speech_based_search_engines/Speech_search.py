import speech_recognition as sr
import webbrowser

def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Please say your search query...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Use Google Web Speech API
        query = recognizer.recognize_google(audio)
        print(f"Recognized query: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your voice.")
    except sr.RequestError:
        print("Speech Recognition service is unavailable.")
    return None

def search_web(query):
    if query:
        # Replace spaces with '+' for URL formatting
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        print(f"Searching for: {query}")
        webbrowser.open(url)

if __name__ == "__main__":
    query = recognize_speech()
    search_web(query)
