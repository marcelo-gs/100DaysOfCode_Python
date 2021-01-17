from bs4 import BeautifulSoup
import requests
import spotipy 
from spotipy.oauth2 import SpotifyOAuth



SPOTIPY_CLIENT_ID="-"
SPOTIPY_CLIENT_SECRET="-"
SPOTIPY_REDIRECT_URI = "http://example.com"

scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, 
                                               client_id=SPOTIPY_CLIENT_ID, 
                                               client_secret=SPOTIPY_CLIENT_SECRET, 
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               show_dialog=True,
                                               cache_path="token.txt"))

user_id = sp.current_user()["id"]
#dod5b3531ygaobua4li144qu2
print(user_id)
date = input("Witch year do you want to travel? Type the date in this format YYYY-MM-DD:")
url = "https://www.billboard.com/charts/hot-100/" + date
print(url)
response = requests.get(url)
response.raise_for_status()
billaboard = response.text
soup = BeautifulSoup(billaboard, "html.parser")

titles = soup.find_all(name="span", class_="chart-element__information")
song_names = [ song.find(name="span", class_="chart-element__information__song text--truncate color--primary").getText()  for song in titles]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    #print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist_name = f"{date} Billboard 100"    
playlist_id = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description="By Marcelo Gomes on Python")
sp.user_playlist_add_tracks(user_id, playlist_id, tracks=song_uris)

