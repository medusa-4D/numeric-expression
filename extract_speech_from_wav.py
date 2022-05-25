import wave
import json
from tqdm import tqdm
from pathlib import Path
from vosk import Model, KaldiRecognizer

model_path = "models/vosk-model-en-us-0.22"
model = Model(model_path)
words = ['huge', 'tiny']

wavs = sorted(list(Path('.').glob('data/wavs/*.wav')))
for wav in wavs:
    print(wav)
    wf = wave.open(str(wav), "rb")
    frame_rate = wf.getframerate()
    n_frames = wf.getnframes()
    
    rec = KaldiRecognizer(model, frame_rate)#, words)
    rec.SetWords(True)

    results = []
    n_iters = n_frames // 4000

    for i in tqdm(range(n_iters)):
        data = wf.readframes(4000)
        
        if len(data) == 0:
            break
        
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            det_words = [r['word'] for r in res['result']]
            print(det_words)
            if 'huge' in det_words:
                print(res)
            
    print(rec.FinalResult())    
    wf.close()