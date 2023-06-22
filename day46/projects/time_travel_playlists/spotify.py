import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import SPOTIFY


class Spotify():
    def __init__(self, date) -> None:
        self.base_url = "https://api.spotify.com/v1"
        self.auth_url = "https://accounts.spotify.com/"
        self.id = SPOTIFY["id"]
        self.user_id = SPOTIFY["user_id"]
        self.secret = SPOTIFY["secret"]

        self.date = date

    def get_auth_token(self):
        sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://example.com",
            client_id=self.id,
            client_secret=self.secret,
            show_dialog=True,
            cache_path="token.txt"
            )
        )
        user_id = sp.current_user()["id"]

    def search_song_uri(self, song_names):
        song_uris = []
        year = date.split("-")[0]
        for song in song_names:
            result = sp.search(q=f"track:{song} year:{year}", type="track")
            print(result)
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")