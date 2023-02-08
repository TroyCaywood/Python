import requests
import os
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

# Connection variables for spotipy
SPOTIPY_CLIENT_ID = os.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = "http://example.com"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Create soup from billboard 100 using date input
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(URL)
bb_webpage = response.text
soup = BeautifulSoup(bb_webpage, "html.parser")

# Find all songs using h3 class and ID. First song had different class so find it as well. Add all songs to a list by getting text from tag and strip extra spaces. Insert first song at the beginning of the list.
songs = soup.findAll(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only", id="title-of-a-story")
first_song = soup.find(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet", id="title-of-a-story").getText()
first_song = first_song.replace("\n", "")
songs_list = [song.getText().strip() for song in songs]
songs_list.insert(0, first_song.strip())

# OAUTH connection parameters for spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=f"{SPOTIPY_CLIENT_ID}",
        client_secret=f"{SPOTIPY_CLIENT_SECRET}",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt",
        redirect_uri="http://example.com",
    )
)

# Get current user ID
user_id = sp.current_user()["id"]

# Get just the year from date variable, take each song in the song list and search for the song during that year on spotify. Try to get song URI, if URI doesnt exist skip song.
song_uris = []
year = date.split("-")[0]
for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Create playlist using current user id, name the playlist using the date entered + Billboard 100 and make the playlist private. Then add the songs to that playlist using the URIs from the song_uris list.
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

