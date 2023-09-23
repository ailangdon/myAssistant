# myAssistant
This is a project to create a personal assistant. The project progress is documented in several Medium articles. It is an attempt to build my personal assistant which is voice controlled, can execute some of the standard actions (e.g. play music, set timer, etc.) and can answer questions based on LLMs.

The current v0.1 PoC stage can be checked out with the command:
```bash
git checkout 0.1
```

## Pre-requisites
An API Key for OpenAI ChatGPT needs to be provided in the environment variable `OPENAI_API_KEY`. The application uses the `gpt-3.5-turbo` model. In addition an access key for Pico Voice Wake Word Detection needs to be provided in the environment variable `PICOVOICE_ACCESS_KEY`. Access key can be created on the Picovoice site https://picovoice.ai for free.

The access keys can be provided in a .env file:
```bash
PICOVOICE_ACCESS_KEY=
OPENAI_API_KEY=
```

This project has been developed on Ubuntu 22.04. No other OS has been tested, run on your own risk.


## Installation
On Ubuntu install the portaudio development package:
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
The name of the assistant can be specified as command line argument. The default name is Jarvis. You can run the application with the following command:
```bash
python Assistant.py [name]
```
The name has to be one of the wake words available by default in picovoice: `grapefruit`, `hey siri`, `picovoice`, `blueberry`, `bumblebee`, `hey barista`, `hey google`, `snowboy`, `americano`, `view glass`, `alexa`, `pico clock`, `terminator`, `computer`, `jarvis`, `porcupine`, `grasshopper`, `smart mirror`, `ok google`.

On the first run, the application will download multiple models (for wake word, speech recognition and speech generation). This may take a while.

Say "Jarvis" or the name you specified on the command line to initate the conversation. After the "yes" confirmation you have 6 seconds to speak with the assistant. After that, the assistant will generate a response and say it out loud.

Depending on the hardware each application the speech recognition and generation steps can take a while.

## References
The following projects were used:
* Picovoice Porcupine Wake Word Engine Demos https://github.com/Picovoice/porcupine/tree/master/demo/python
* whisper_mic https://github.com/mallorbc/whisper_mic and model from https://huggingface.co/spaces/openai/whisper
* Langchain https://python.langchain.com/
* Fast2speech https://huggingface.co/facebook/fastspeech2-en-ljspeech

It is amazing how much functionality is available in this exciting domain. Thanks to all the contributors!