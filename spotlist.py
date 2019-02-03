from clients.setlist import SetlistClient
from clients.spotify import SpotifyClient


class SpotlistClient:

    def __init__(self, setlist_key: str, spotify_username: str, spotify_id: str, spotify_secret: str):
        self._setlist = SetlistClient(api_key=setlist_key)
        self._spotify = SpotifyClient(spotify_username, spotify_id, spotify_secret)

    def playlist_from_latest_gig(self, artist: str, name: str = None, public: bool = False):
        songs = self._setlist.get_latest_setlist_for_artist(artist)
        self._spotify.create_artist_playlist(artist, songs, name, public)

    def playlist_from_last_gigs(self, artist: str, n: int, name: str = None, public: bool = False):
        songs = self._setlist.create_setlist_from_last_gigs(artist, n)
        self._spotify.create_artist_playlist(artist, songs, name, public)

    def playlist_from_specific_gig(self, artist: str, date: str, name: str = None, public: bool = False):
        songs = self._setlist.get_specific_setlist_for_artist(artist, date)
        self._spotify.create_artist_playlist(artist, songs, name, public)
