# numeric-expression

Code for the 'numeric-expression' project. The dataset with video URLs (in `data/data.csv`) was composed by [Greg Woodin and colleagues (2020)](https://doi.org/10.1371/journal.pone.0242142) and is available [here](https://osf.io/dncjg/).

## Dataset curation

1. Install Python requirements (`pip install -r requirements.txt`)
2. Downloaded the videos (`python download_videos.py`)
3. Extract audio (WAV) track (`bash extract_wav_from_videos.sh`)
4. Extract speech from audio (`python extract_speech_from_wav.py`)
5. Find events in speech transcription (TODO)
