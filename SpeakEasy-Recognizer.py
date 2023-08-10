import speech_recognition as speech
import tkinter as tk
from tkinter import messagebox

def start_recording():
    with speech.Microphone() as voice:
        speak.adjust_for_ambient_noise(voice)
        status_label.config(text="Recording...", fg="blue")
        status_label.update()

        audio = speak.listen(voice)

        status_label.config(text="Recognizing...", fg="orange")
        status_label.update()

        try:
            recognized_text = speak.recognize_google(audio)
            recognized_text_label.config(text="You said:", fg="green")
            recognized_text_value.config(text=recognized_text, fg="green")

        except Exception as e:
            recognized_text_label.config(text="Error:", fg="red")
            recognized_text_value.config(text=str(e), fg="red")

        write_audio_to_file(audio)
        status_label.config(text="Finished recording", fg="green")
        status_label.update()

def write_audio_to_file(audio):
    with open("recorded.wav", "wb") as f:
        f.write(audio.get_wav_data())

def main():
    global speak, status_label, recognized_text_label, recognized_text_value
    speak = speech.Recognizer()

    root = tk.Tk()
    root.title("Speech Recognition Program")

    header_label = tk.Label(root, text="Speech Recognition Program", font=("Helvetica", 16))
    header_label.pack(pady=10)

    start_button = tk.Button(root, text="Start Recording", command=start_recording, bg="blue", fg="white")
    start_button.pack(pady=10)

    status_label = tk.Label(root, text="", font=("Helvetica", 12))
    status_label.pack(pady=5)

    recognized_text_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"))
    recognized_text_label.pack(pady=5)

    recognized_text_value = tk.Label(root, text="", font=("Helvetica", 12))
    recognized_text_value.pack(pady=5)

    quit_button = tk.Button(root, text="Quit", command=root.destroy, bg="red", fg="white")
    quit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
