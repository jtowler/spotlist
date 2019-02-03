# spotlist

Create Spotify Playlists of Real Gigs

`SpotListClient` currently requires a Setlist.fm api key, a spotify username, client id and secret. 
It supports the following methods:
   * `playlist_from_latest_gig(self, artist, name, public)`
       * Create a playlist from the last gig the artist played
   * `playlist_from_last_gigs(self, artist, n, name, public)`
       * Create a playlist from the last n gigs the artist has played
   * `playlist_from_specific_gig(self, artist, date, name, public)`
       * Create a playlist from the gig the artist played on a  specific date
   