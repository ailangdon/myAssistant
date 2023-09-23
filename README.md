# myAssistant
This is a project to create a personal assistant. The project progress is documented in several Medium articles. It is an attempt to rebuild my personal assistant which is voice controlled, can execute some of the standard actions (e.g. play music, set timer, etc.) and can answer questions based on LLMs.

The current v0.1 PoC stage can be checked out with the command:
```bash
git checkout 0.1
```

## Pre-requisites
You need an API Key for OpenAI ChatGPT, the software uses the environment variable OPENAI_API_KEY to get the key. The software uses the ChatGPT 3.5 model. In addition you also need an access key for Pico Voice Wake Word Detection. The software uses the environment variable PICOVOICE_ACCESS_KEY to get the key. You can get an access key here: https://picovoice.ai. 

You can also create a .env file with the two variables:
```bash
PICOVOICE_ACCESS_KEY=
OPENAI_API_KEY=
```

This project has been developed on Ubuntu 22.04. No other OS has been tested, run on your own risk.


## Installation
On Ubuntu install portaudio development package:
```bash
sudo apt-get install portaudio19-dev
```

Install python dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run
You can specify the name of the assistant as a command line argument. The default name is Jarvis. You can run the application with the following command:
```bash
python Assistant.py [name]
```
The name has to be one of the wake words available by default in picovoice: `grapefruit`, `hey siri`, `picovoice`, `blueberry`, `bumblebee`, `hey barista`, `hey google`, `snowboy`, `americano`, `view glass`, `alexa`, `pico clock`, `terminator`, `computer`, `jarvis`, `porcupine`, `grasshopper`, `smart mirror`, `ok google`.

On the first run, the application will download multiple models (for wake word, speech recognition and speech generation). This may take a while.

Say "Jarvis" or the name you specified on the command line to wake up the assistant. After the "yes" confirmation you have 6 seconds to speak with the assistant. After that, the assistant will generate a response and speak to you.

Depending on your hardware each application step especially speech recognition and generation can take a while.

## Thanks
Thanks to the following projects which were used in this project:
* Picovoice Porcupine Wake Word Engine Demos https://github.com/Picovoice/porcupine/tree/master/demo/python
* whisper_mic https://github.com/mallorbc/whisper_mic and model from https://huggingface.co/spaces/openai/whisper
* Langchain https://python.langchain.com/
* Fast2speech https://huggingface.co/facebook/fastspeech2-en-ljspeech



