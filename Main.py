import torch
import numpy as np
import speech_recognition as sr
#from gpt import gpt
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import json
import pyaudio

class NeuralSpeaker: # There a model for voice acting your text
    def __init__(self):
        device = torch.device('cpu') # CPU/CUDA (gpu)
        local_file = 'model.pt'  # Adjust the path to your model file
        # I download model there 'https://models.silero.ai/models/tts/ru' #
        # 'v3_1_ru' model not bagging so im use him
        self.__model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
        self.__model.to(device)

    def speak(self, words, speaker='baya', sample_rate=48000): # Russian speakers available: aidar, baya, kseniya, xenia, eugene, random
        audio = self.__model.apply_tts(text=words, speaker=speaker, sample_rate=sample_rate)
        audio = audio.numpy()
        audio *= 32767 / np.max(np.abs(audio))
        audio = audio.astype(np.int16)
        return audio

    def input_and_speak(self, text):
        input_text = (text)  # Give text to GPT
        audio_data = self.speak(input_text)

        sd.play(audio_data, 48000, device=8)  # Playing file to virtual Microphone
        sd.wait()  # Wait ending

        # Saving file can take so much time
        """
        import wave
        import simpleaudio as sa
        import soundfile as sf
        
        # Saving to file
        with wave.open(f="Audio.mp3", mode="wb") as file:
            file.setnchannels(1)  # Mono
            file.setsampwidth(2)  # 2 bite on Sample
            file.setframerate(48000) # Hhz (If you make Hhz too low, it can become rougher and more bass)
            file.writeframes(audio_data) 

            fs = sf.read('Audio.mp3') # Reading us Audio
            # CHANGE #CHANGE #CHANGE #CHANGE #CHANGE #CHANGE #CHANGE #CHANGE #CHANGE #CHANGE #CHANGE #CHANGE #CHANGE
            sd.play(data, fs, device=8) # Playing file to virtual Microphone
            sd.wait() # Wait ending
        """


# CHANGE #CHANGE #CHANGE #CHANGE #CHANGE #CHANGE #CHANGE #CHANGE #CHANGE #CHANGE #CHANGE #CHANGE #CHANGE
with sr.Microphone(device_index=2) as source: # There need change device index to your
    model = Model("vosk-model-small-ru-0.22") # Adding VOSK model
    recognizer = KaldiRecognizer(model, 16000)
    # CHANGE #CHANGE #CHANGE #CHANGE #CHANGE #CHANGE #CHANGE #CHANGE #CHANGE #CHANGE #CHANGE #CHANGE #CHANGE
    stream = pyaudio.PyAudio().open(format=pyaudio.paInt16,
                                    channels=1,
                                    rate=16000,
                                    input=True,
                                    frames_per_buffer=8000,
                                    input_device_index=2)
    print("Test 2/2 | Success, You can start Talk")
    while True:
        stream.start_stream() # Start hear you voice in start and after GPT give answer
        data = stream.read(4000)
        if recognizer.AcceptWaveform(data) and len(data) > 0:
            # Start using VOSK model
            answer = recognizer.Result() # What we got
            result_dict = json.loads(answer) # Some changes
            text = result_dict.get("text", "") # lear Text
            # End using VOSK model
            stream.stop_stream() # Stop hear, because your GPT have time to give answer, and we wait this
            if text != "": # I don't using 'answer' because he has another symbols, so im slash him and using in 'text'
                print('Vosk model text: ' + text)  # Print what model is hear
                speaker = NeuralSpeaker() # Give text to Voice Model
                speaker.input_and_speak(text)  # Discord talking