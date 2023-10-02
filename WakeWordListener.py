import os
from datetime import datetime
import pvporcupine
from pvrecorder import PvRecorder

class WakeWordListener:

    def __init__(self, wakeword, access_key) -> None:
        self.picovoice_access_key = access_key
        self.wake_word = wakeword
        self.sensitivities = [0.5] * 1 # multiply with number of keywords
        self.create_porcupine()

    def create_porcupine(self):
        try:
            keyword_paths = [pvporcupine.KEYWORD_PATHS[self.wake_word]]
            # create porcupine object, use default library_path and model_path
            self.porcupine = pvporcupine.create(
                access_key=self.picovoice_access_key,                
                keyword_paths=keyword_paths,
                sensitivities=self.sensitivities)
        except pvporcupine.PorcupineInvalidArgumentError as e:
            print("One or more arguments provided to Porcupine is invalid: ")
            print("If all other arguments seem valid, ensure that '%s' is a valid AccessKey" % self.picovoice_access_key)
            raise e
        except pvporcupine.PorcupineActivationError as e:
            print("AccessKey activation error")
            raise e
        except pvporcupine.PorcupineActivationLimitError as e:
            print("AccessKey '%s' has reached it's temporary device limit" % self.picovoice_access_key)
            raise e
        except pvporcupine.PorcupineActivationRefusedError as e:
            print("AccessKey '%s' refused" % self.picovoice_access_key)
            raise e
        except pvporcupine.PorcupineActivationThrottledError as e:
            print("AccessKey '%s' has been throttled" % self.picovoice_access_key)
            raise e
        except pvporcupine.PorcupineError as e:
            print("Failed to initialize Porcupine")
            raise e

        keywords = list()
        for x in keyword_paths:
            keyword_phrase_part = os.path.basename(x).replace('.ppn', '').split('_')
            if len(keyword_phrase_part) > 6:
                keywords.append(' '.join(keyword_phrase_part[0:-6]))
            else:
                keywords.append(keyword_phrase_part[0])

        print('Porcupine version: %s' % self.porcupine.version)

        audio_device_index=-1
        self.recorder = PvRecorder(
            frame_length=self.porcupine.frame_length,
            device_index=audio_device_index)

    def cleanup(self):
        self.porcupine.delete()
        self.recorder.delete()

    def listen_for_keyword(self):
        self.recorder.start()
        
        print('Listening ... (press Ctrl+C to exit)')

        wake_word_detected = False
        while not wake_word_detected:
            pcm = self.recorder.read()
            result = self.porcupine.process(pcm)

            if result >= 0:
                wake_word_detected = True
                print('[%s] Detected %s' % (str(datetime.now()), self.wake_word))

        self.recorder.stop()
