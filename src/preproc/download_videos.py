import requests
import pandas as pd
from tqdm import tqdm
from pathlib import Path

data = pd.read_csv('data/data.csv', encoding='latin1')
for idx, row in tqdm(data.iterrows(), total=data.shape[0]):
    id_ = row['ID']
    f_out = Path(f'data/videos/{id_}.mp4')
    if f_out.is_file():
        continue

    try:
        r = requests.get(row['URL'])
        with open(str(f_out), 'wb') as fd:
            fd.write(r.content)
    except requests.exceptions.ConnectionError as e:
        print(f"Could not download {row['URL']}!")
