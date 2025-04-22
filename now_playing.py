import requests

# 🎧 Fetch the latest track played on KEXP
track = requests.get("https://api.kexp.org/v2/plays/?format=json&limit=1&ordering=-airdate").json()["results"][0]

# 🎶 Extract artist, song, and album
artist = track['artist']
song = track['song']
album = track.get('album', 'Unknown Album')

# 🌈 Print it nicely with colors and emojis
print(f"\033[1;35m🎶 Now Playing on KEXP\033[0m\n"
      f"\033[1;34m🎤 Artist:\033[0m {artist}\n"
      f"\033[1;32m🎵 Song:\033[0m   {song}\n"
      f"\033[1;33m💿 Album:\033[0m  {album}")
