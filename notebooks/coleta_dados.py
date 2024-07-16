import lyricsgenius
import json

genius = lyricsgenius.Genius("YOUR_GENIUS_ACCESS_TOKEN")
artist = genius.search_artist("Bob Marley", max_songs=50, sort="popularity")
songs = artist.songs

data = []
for song in songs:
    data.append({
        "title": song.title,
        "lyrics": song.lyrics,
        "album": song.album,
        "year": song.year
    })

with open('dados/bruto/musicas.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
