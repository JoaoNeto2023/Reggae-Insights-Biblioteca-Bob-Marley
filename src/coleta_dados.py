import lyricsgenius
import json
from requests.exceptions import Timeout

# Substitua 'YOUR_GENIUS_ACCESS_TOKEN' pelo token que você forneceu
TOKEN = "8OfSJqjMmDdN7rciAUXywGGzro3fwvOBM46CbqY66GS9LqBdVZiLs_uaJb9VDhKj"
genius = lyricsgenius.Genius(TOKEN, timeout=15)  # Aumentar o timeout para 15 segundos

try:
    print("Searching for songs by Bob Marley...")
    artist = genius.search_artist("Bob Marley", max_songs=50, sort="popularity")
    songs = artist.songs

    data = []
    for song in songs:
        data.append({
            "title": song.title if hasattr(song, 'title') else None,
            "lyrics": song.lyrics if hasattr(song, 'lyrics') else None,
            "album": song.album if hasattr(song, 'album') else None,
            "year": song.year if hasattr(song, 'year') else None
        })

    with open('dados/bruto/musicas.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Data collection completed successfully.")
except Timeout:
    print("A solicitação para a API do Genius excedeu o tempo limite. Tente aumentar o timeout ou verificar sua conexão.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
