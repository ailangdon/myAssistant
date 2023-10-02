import sys
import os
from dotenv import load_dotenv
from QueryProcessor import QueryProcessor
from TextToSpeech import TextToSpeech
from SpeechToText import SpeechToText
from WakeWordListener import WakeWordListener
from utils import start_timer, elapsed_time

load_dotenv()

class MyAssistant:

    def __init__(self, name) -> None:        
        self.wake_word_listener = WakeWordListener(name, os.getenv("PICOVOICE_ACCESS_KEY"))
        self.speech_to_text = SpeechToText()
        self.query_processor = QueryProcessor(os.getenv("OPENAI_API_KEY"))
        self.text_to_speech = TextToSpeech()        

    def run(self):
        try:
            while True:
                self.listen_for_keyword()
                start_timer("main")
                self.respond_with_yes_man()
                elapsed_time("main", "Saying yes")
                query = self.listen_to_question() 
                elapsed_time("main", "Speech to text")               
                response = self.think_about_a_response(query)
                elapsed_time("main", "LLM")
                print("Response "+str(response))                
                self.respond_with_response(response)                
                elapsed_time("main", "Text to speech")
        except KeyboardInterrupt:
            self.cleanup()

    def cleanup(self):
        self.wake_word_listener.cleanup()
        self.text_to_speech.cleanup()
        
    def listen_for_keyword(self):
        self.wake_word_listener.listen_for_keyword()
        
    def respond_with_yes_man(self):
        self.text_to_speech.yes()

    def listen_to_question(self):
        query = self.speech_to_text.listen(timeout=7)
        print(query)        
        return query
    
    def think_about_a_response(self, query):
        response = self.query_processor.process(query)
        return response
    
    def respond_with_response(self, text):
        self.text_to_speech.speak(text)

if __name__ == "__main__":
    name = 'jarvis'
    if len(sys.argv)>1:
        name = sys.argv[1]
    myAssistant = MyAssistant(name)
    myAssistant.run()
