import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import urllib

client_credentials_manager = SpotifyClientCredentials(client_id='2b211ac7629d41699c48e4c5a9098ee3', client_secret='1373301210f141a1a9b7a60c684c5e05')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.user_playlists(user='1284712885')
count = -1
while playlists:
	for i, playlist in enumerate(playlists['items']):
		count += 1
		try:
			urllib.request.urlretrieve(playlist['images'][0]['url'], filename='images/' + str(count) + '.jpeg')
		except IndexError:
			pass
	if playlists['next']:
		playlists = sp.next(playlists)
	else:
		playlists = None