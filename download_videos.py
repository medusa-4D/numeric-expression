import requests
import pandas as pd
from tqdm import tqdm

data = pd.read_csv('data/data.csv', encoding='latin1')
for idx, row in tqdm(data.iterrows(), total=data.shape[0]):
    id_ = row['ID']
    r = requests.get(row['URL'])

    with open(f'data/videos/{id_}.mp4', 'wb') as fd:
        fd.write(r.content)
