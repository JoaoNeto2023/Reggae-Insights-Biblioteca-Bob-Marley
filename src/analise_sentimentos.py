import json
import pandas as pd
from textblob import TextBlob

# Carregar os dados das músicas
with open('dados/bruto/musicas.json', 'r') as f:
    data = json.load(f)

# Função para obter o sentimento da letra
def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

# Adicionar a análise de sentimentos aos dados
for song in data:
    if song['lyrics']:  # Verifica se há letras disponíveis
        song['sentiment'] = get_sentiment(song['lyrics'])
    else:
        song['sentiment'] = None

# Converter os dados em um DataFrame do Pandas
df = pd.DataFrame(data)

# Salvar os dados processados
df.to_csv('dados/processado/musicas_sentimentos.csv', index=False)

print("Análise de sentimentos concluída com sucesso.")
