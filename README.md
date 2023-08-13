# Speech Recognition Program

This is a simple Python program that utilizes the `speech_recognition` library to perform speech recognition and record audio from a microphone.

## How it Works

The program uses the `speech_recognition` library to capture audio from the microphone and then attempts to recognize the spoken words using Google's speech recognition API. If successful, it displays the recognized text on the interface.

## Dependencies

Make sure you have the following dependencies installed before running the program:

- `speech_recognition`
- `tkinter`

You can install them using the following:

bash
`pip install SpeechRecognition`

## Usage

- Run the script `SpeakEasy-Recognizer.py`.
- 
- Click the "Start Recording" button to begin capturing audio from the microphone.
- 
- The program will display the recording and recognition statuses.
- 
- If successful, the recognized text will be displayed.
- 
- The recorded audio will be saved as "recorded.wav" in the same directory.


## Note

- If an error occurs during recognition, it will be displayed.
- 
- The adjust_for_ambient_noise function helps to set ambient noise levels before recording.
- 
- The program provides a graphical interface using `tkinter`.

- 
## Contributing

Contributions are welcome! Feel free to submit issues or pull requests if you find any problems or have suggestions for improvement.

