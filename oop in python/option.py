import speech_recognition as sr
import pyttsx3
import tkinter as tk

# Initialize speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to speak a response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to recognize speech and respond
def listen():
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # Adjust the pause threshold to account for background noise
        audio = r.listen(source, phrase_time_limit=5)

        try:
            # Use Google Speech Recognition to transcribe audio
            text = r.recognize_google(audio)
            print(f"User said: {text}")
            # Echo the user's speech back to them
            speak(f"You said: {text}")
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again.")
            speak("Sorry, I didn't catch that. Please try again.")
        except sr.RequestError:
            print("Sorry, my speech service is down. Please try again later.")
            speak("Sorry, my speech service is down. Please try again later.")

# Create a GUI window
window = tk.Tk()
window.title("Voice Assistant")

# Create a label and a button to listen for speech
label = tk.Label(window, text="Press the button and speak")
label.pack()
button = tk.Button(window, text="Listen", command=listen)
button.pack()

# Start the GUI event loop
window.mainloop()

