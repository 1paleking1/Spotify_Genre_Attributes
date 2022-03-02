from http import client
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import json


auth_manager = SpotifyClientCredentials(
    client_id='ID',
    client_secret='SECRET'
)

sp = spotipy.Spotify(auth_manager=auth_manager)


tracks = sp.playlist_tracks(
    playlist_id='37i9dQZF1DX76Wlfdnj7AP',
    market='AO'
)

with open('mellow_bars.json', 'w') as file:
    file.write(json.dumps(tracks, indent=4))


track_ids__ = [tracks['items'][count]['track']['id'] for count in range(tracks['total']-tracks['limit'])]
track_ids = []

for i, n in enumerate(tracks['items']):
    print(i)
    val = n[i]['track']['id']
    track_ids.append(val)
    if tracks['next']:
        tracks = sp.next(tracks)
    else:
        tracks = None


print(len(track_ids))
