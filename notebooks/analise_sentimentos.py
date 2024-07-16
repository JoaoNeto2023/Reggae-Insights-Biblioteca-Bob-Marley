import json
import pandas as pd
from textblob import TextBlob

with open('dados/bruto/musicas.json', 'r') as f:
    data = json.load(f)

def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

for song in data:
    song['sentiment'] = get_sentiment(song['lyrics'])

df = pd.DataFrame(data)
df.to_csv('dados/processado/musicas_sentimentos.csv', index=False)
