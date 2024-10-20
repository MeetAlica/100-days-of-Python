from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from your_data import CLIENT_ID, CLIENT_SECRET

# Constants
DATE = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
HEADER = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
URL = "https://www.billboard.com/charts/hot-100/" + DATE
MY_REDIRECT_URI="https://open.spotify.com/"

# Scraping Billboard 100
response = requests.get(url=URL, headers=HEADER)
soup = BeautifulSoup(response.text, "html.parser")
song_names_tags = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_tags]

# Spotify Auth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=MY_REDIRECT_URI,
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt"
))
user_id = sp.current_user()["id"]

# Searching songs on Spotify
song_uris = []
year = DATE.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{DATE} Billboard 100", public=False)

# Adding songs to the playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


print("The playlist is ready. Enjoy listening. :)")
