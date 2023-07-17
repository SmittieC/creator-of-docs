# creator-of-docs
A simple commandline tool to help create technical documentation from audio / text. This is meant to help save time.


## Setup
### Requirements
OpenAI token, so a paid OpenAI account


### Create virtual environment
> pip -m venv venv

### Install dependencies

> source venv/bin/activate
> 
> make install

## Usage
### Create transcriptions
You can create transcriptions from audio by copying the audio file into the script's directory and running
> `make create_transcription`

This will create a `text.txt` file containing the transcription. Be sure to double check the transcription before
creating the documentation.

Note: The first time you run this command will take a short while. The whisper model is downloaded first.

### Create documentation
Running
> make create_doc

will read the `text.txt` file in the script's directory and create a new file with the created documentation.
The file name is fixed to `doc.txt`.
