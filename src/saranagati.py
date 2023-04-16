# %%
import requests
from blackhole import Song, Playlist
from iskcondesiretree import get_duration

# %%
def get_saranagati():
    url = "https://bhaktivinodainstitute.org/?audioigniter_playlist_id=4397"
    response = requests.get(url)
    return response.json()

def parse_playlist(playlist):
    tracks = []
    for track in playlist:
        # Album: Compisition
        # Artist: Bhaktivinoda Thakur
        # Genre: Singer
        tracks.append(Song(
            url = track['downloadUrl'],
            perma_url = track['downloadUrl'],
            image = track['cover'],
            title = track['title'],
            album = 'Saranagati', 
            duration = get_duration(track['downloadUrl']),
            artist = 'Bhaktivinoda Thakur',
            subtitle = 'Kirtan',
            genre='Unknown'
        ))
        
    return tracks

# %%
playlist_data = get_saranagati()
tracks = parse_playlist(playlist_data)
Playlist('Saranagati', tracks).createJSON()

# %%
