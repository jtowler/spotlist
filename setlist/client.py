import requests as re
from typing import List


class SetlistClient:
    _base_string = "https://api.setlist.fm/rest/1.0/"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self._headers = {'x-api-key': api_key,
                         'Accept': 'application/json'}

    def get_latest_setlist_for_artist(self, artist: str) -> List[str]:
        mbid = self.get_artist_id(artist)
        query = f"artist/{mbid}/setlists?p=1"
        response = self._query(query)
        sets = response['setlist'][0]['sets']['set']
        songs = self._setlist_to_set(sets)
        return songs

    def get_specific_setlist_for_artist(self, artist: str, date: str) -> List[str]:
        mbid = self.get_artist_id(artist)
        p = 1
        while True:
            query = f"artist/{mbid}/setlists?p={p}"
            response = self._query(query)
            for st in response['setlist']:
                if st['eventDate'] == date:
                    songs = self._setlist_to_set(st['sets']['set'])
                    return songs
                elif st['eventDate'] < date:
                    return []
            p += 1

    @staticmethod
    def _setlist_to_set(setlist: dict) -> List[str]:
        songs = []
        for st in setlist:
            for song in st['song']:
                if song not in songs:
                    songs.append(song['name'])
        return songs

    def get_artist_id(self, artist: str) -> str:
        query = f"search/artists?p=1&artistName={artist}&sort=relevance"
        response = self._query(query)
        return response['artist'][0]['mbid']

    def _query(self, query: str) -> dict:
        res = re.get(f"{self._base_string}{query}", headers=self._headers)
        if res.status_code != 200:
            raise Exception(f"Query failed with code [{res.status_code}]")
        return res.json()
