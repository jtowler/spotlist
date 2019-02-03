from typing import List
import spotipy
import spotipy.util as util


class SpotifyClient:
    def __init__(self, username: str, client_id: str, client_secret: str):
        self.username = username
        token = util.prompt_for_user_token(username,
                                           'playlist-modify-private playlist-modify-public',
                                           client_id,
                                           client_secret,
                                           "http://localhost:8888/callback/")
        self._client = spotipy.Spotify(auth=token)

    def get_song_id(self, name: str, artist: str) -> str:
        response = self._client.search(q=f"artist: {artist}, track: {name}", type='track')
        try:
            return response['tracks']['items'][0]['id']
        except IndexError:
            raise SpotifyError(f"Did not find track {name} by {artist}")

    def create_artist_playlist(self, artist: str, songs: List[str], name: str = None,
                               public: bool = False) -> None:
        if name is None:
            name = artist
        playlist = self._client.user_playlist_create(self.username, name, public)
        ids = []
        for song in songs:
            try:
                ids.append(self.get_song_id(song, artist))
            except SpotifyError as e:
                print(str(e))
        tracks = ["spotify:track:" + track for track in ids]
        self._client.user_playlist_add_tracks(self.username, playlist['id'], tracks)


class SpotifyError(Exception):
    def __init__(self, message):
        super().__init__(message)
