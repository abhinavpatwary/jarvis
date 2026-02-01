import speech_recognition as sr
import pyttsx3
import webbrowser
import pyjokes
import sys
import time


WAKE_WORD = "jarvis"
LANGUAGE = "en-IN"


engine = pyttsx3.init()
engine.setProperty("rate", 180)

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()


def listen_once():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.4)
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language=LANGUAGE).lower()
        print("YOU SAID:", text)
        return text
    except:
        return ""


def clean_command(text):
    noise_words = ["please", "now", "can you", "could you", "tell me"]
    for word in noise_words:
        text = text.replace(word, "")
    return " ".join(text.split())


print("STARTING JARVIS")

spoken = listen_once()

if WAKE_WORD not in spoken:
    speak("Wake word not detected")
    print("END")
    sys.exit(0)

speak("Yes")


command = spoken.replace(WAKE_WORD, "")
command = clean_command(command)


if command == "":
    command = clean_command(listen_once())

if command == "":
    speak("No command received")
    print("END")
    sys.exit(0)

print("FINAL COMMAND:", command)
if "open google" in command:
    speak("Opening Google")
    time.sleep(1)
    webbrowser.open("https://www.google.com")

elif "open youtube" in command:
    speak("Opening YouTube")
    time.sleep(1)
    webbrowser.open("https://www.youtube.com")

elif "open spotify" in command:
    speak("Opening Spotify")
    time.sleep(1)
    webbrowser.open("https://open.spotify.com")


elif "search" in command:
    query = command.replace("search", "").strip()
    speak(f"Searching for {query}")
    time.sleep(1)
    webbrowser.open(f"https://www.google.com/search?q={query}")


elif "joke" in command:
    speak(pyjokes.get_joke())

elif "note" in command or "remember" in command:
    note = command.replace("note", "").replace("remember", "").strip()
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
    speak("Note saved successfully")

else:
    speak("Sorry, I did not understand the command")

#END
speak("Done")
print("END")
sys.exit(0)
