# Game2Text

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) 

![Game2Text Preview](https://game2text.com/images/header-software-app.png)

[Game2Text](https://www.game2text.com) is an all-in-one application that helps you learn language from games.


## Features
- Dictionary lookup with browser dictionaries like Yomichan
- Translation - DeepL, Papago, and Google
- Create image and audio flashcards via Anki and AnkiConnect

## Download 
You can find downloads on [Releases](https://github.com/mathewthe2/Game2Text/releases).

## FAQ
[Read FAQ](https://github.com/mathewthe2/Game2Text/blob/main/public/faq.md)

## Documentation
[Read Documentation](https://github.com/mathewthe2/Game2Text/blob/main/public/documentation.md)

## Prerequisite: Tesseract

Windows/Mac: Tesseract is bundled with the application.

Linux: Follow installation instructions [here](https://tesseract-ocr.github.io/tessdoc/Home.html).

## Getting Started

Create a venv, then once activated install requirements:
```
pip install -r requirements.txt
python game2text.py
```

On Windows, install pyaudio_portaudio through wheel. This package includes "as_loopback" as an option to record system audio through Windows WASAPI. 
```
pip uninstall pyaudio
pip install https://github.com/intxcc/pyaudio_portaudio/releases/download/1.1.1/PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
```

## Distribution

Unzip *resources/sudachidict_small.zip*

Windows: 

```build.bat```

Mac:

```sh build.sh```

Temporary fix for all read/write operations using *os.path* on Mac builds with pyinstaller: create a wrapper file that runs the Game2Text executable inside the package

