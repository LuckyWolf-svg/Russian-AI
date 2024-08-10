import speech_recognition as sr
from gpt import gpt
import sounddevice as sd
import soundfile as sf
from vosk import Model, KaldiRecognizer
import json
import pyaudio
import pyttsx3

with sr.Microphone(device_index=2) as source:
    model = Model("/vosk-model-small-ru-0.22")
    recognizer = KaldiRecognizer(model, 16000)
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)

    print("Начинаю слушать Discord")  # TEST 2

    while True:
        stream.start_stream()
        data = stream.read(4000)

        if recognizer.AcceptWaveform(data) and len(data) > 1:

            answer = recognizer.Result()
            result_dict = json.loads(answer)
            text = result_dict.get("text", "")

            print('text: ' + text)

            stream.stop_stream()

            if text != "":

                filename = '../speechURA.mp3'

                engine = pyttsx3.init()
                engine.setProperty('voice', 'russian')
                engine.save_to_file(gpt(text), filename)
                engine.runAndWait()

                data, fs = sf.read(filename, dtype='float32')
                vb_cable_index = 8
                sd.play(data, fs, device=vb_cable_index)
                sd.wait()