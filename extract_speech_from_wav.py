import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './numeric-face-611c5ff144e9.json'

import json
import wave
from pathlib import Path
from google.cloud import speech

client = speech.SpeechClient()
wavs = sorted(list(Path('.').glob('data/wavs/*.wav')))
for wav in wavs:

    audio = wave.open(str(wav), 'rb')
    frame_rate = audio.getframerate()
    
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=frame_rate,
        language_code="en-US",
        enable_word_time_offsets=True,
    )

    minute = 0
    while True:
        contents = audio.readframes(frame_rate * 60)
        if not contents:
            break

        audio_to_process = speech.RecognitionAudio(content=contents)
        response = client.recognize(config=config, audio=audio_to_process)
        response = type(response).to_json(response)
        
        response = json.loads(response)
        f_out = wav.parents[1] / 'speech'/ (str(wav.stem) + f'_minute-{minute}.json')

        with open(f_out, 'w') as f_out_json:
            json.dump(response, f_out_json, indent=4)

        minute += 1
    exit()