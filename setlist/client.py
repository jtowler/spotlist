import requests as re


class SetlistClient:
    _base_string = "https://api.setlist.fm/rest/1.0/"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self._headers = {'x-api-key': api_key,
                        'Accept': 'application/json'}

    def get_artist_id(self, artist: str) -> str:
        query = f"search/artists?p=1&artistName={artist}&sort=relevance"
        response = self._query(query)
        return response['artist'][0]['mbid']

    def _query(self, query: str) -> dict:
        res = re.get(f"{self._base_string}{query}", headers=self._headers)
        if res.status_code != 200:
            raise Exception(f"Query failed with code [{res.status_code}]")
        return res.json()
