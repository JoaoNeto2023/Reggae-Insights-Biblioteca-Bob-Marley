import requests

TOKEN = "8OfSJqjMmDdN7rciAUXywGGzro3fwvOBM46CbqY66GS9LqBdVZiLs_uaJb9VDhKj"  # Substitua pelo seu token
headers = {
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.get("https://api.genius.com/artists/922?text_format=plain", headers=headers)

if response.status_code == 200:
    print("Token is valid.")
else:
    print(f"Token is invalid. Status code: {response.status_code}")
    print(response.json())
