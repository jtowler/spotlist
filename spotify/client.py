import spotipy
import spotipy.oauth2 as oauth2


class SpotifyClient:
    def __init__(self, client_id: str, client_secret: str):
        auth = oauth2.SpotifyClientCredentials(
            client_id=client_id,
            client_secret=client_secret
        )
        token = auth.get_access_token()
        self.client = spotipy.Spotify(auth=token)

