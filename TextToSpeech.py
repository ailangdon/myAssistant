from fairseq.checkpoint_utils import load_model_ensemble_and_task_from_hf_hub
from fairseq.models.text_to_speech.hub_interface import TTSHubInterface
import pyaudio
from utils import start_timer, elapsed_time

class TextToSpeech:
    def __init__(self):
        self.models, self.cfg, self.task = load_model_ensemble_and_task_from_hf_hub(
            "facebook/fastspeech2-en-ljspeech",
            arg_overrides={"vocoder": "hifigan", "fp16": False, "cpu": True}
        )
        self.model = self.models[0].cpu()
        TTSHubInterface.update_cfg_with_data_cfg(self.cfg, self.task.data_cfg)
        self.generator = self.task.build_generator([self.model], self.cfg)
        self.player = pyaudio.PyAudio()
        self.create_yes()

    def cleanup(self):
        self.stream.close()
        self.player.terminate()

    def create_yes(self):
        self.yes_wav, self.yes_rate = self.generate_wav_data("Yes.")

    def yes(self):
        self.playback(self.yes_wav, self.yes_rate)

    def generate_wav_data(self, text):
        # generate wav
        sample = TTSHubInterface.get_model_input(self.task, text)
        wavdata, rate = TTSHubInterface.get_prediction(self.task, self.model, self.generator, sample)
        output_wav_data = wavdata.numpy().tobytes()         
        return output_wav_data, rate
    
    def playback(self, wav, rate):
        self.stream = self.player.open(format=pyaudio.paFloat32, channels=1, rate=rate, output=True)
        self.stream.write(wav)
        self.stream.stop_stream()
        self.stream.close()

    def speak(self, text):
        start_timer("TTS")
        wav, rate = self.generate_wav_data(text)
        elapsed_time("TTS", "Speech generation")
        self.playback(wav, rate)
        elapsed_time("TTS", "Speech playback")