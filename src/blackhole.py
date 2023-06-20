# %%
import json
import _sha256
from dataclasses import dataclass, asdict
import time
import os


@dataclass  
class Song():
    url: str
    perma_url: str
    title: str
    album: str
    artist: str
    duration: str
    image: str
    subtitle: str

    expire_at: str = None
    release_date: str = None
    genre: str = None
    has_lyrics: str = "false"
    language: str = "en"

    dataAdded: str = None
    id: str = None
    album_id: str = None

    def __post_init__(self):
        self.id = _sha256.sha256(self.url.encode()).hexdigest()[:8] if self.id is None else self.id
        self.album_id = _sha256.sha256(self.album.encode()).hexdigest()[:8] if self.album_id is None else self.album_id
        self.dataAdded = str(int(time.time())) if self.dataAdded is None else self.dataAdded
        self.duration = str(int(self.duration))
    
    def __dict__(self):
        return asdict(self)

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}
    


@dataclass
class Playlist():
    name: str = None
    songs: list[Song] = None
    
    def createJSON(self, path = './'):
        json_contents = json.dumps({song.id: song.__dict__() for song in self.songs}, indent=2)

        with open(os.path.join(path, f"{self.name}.json"), "w") as f:
            f.write(json_contents)

        return True

    def load(self, json_data, name):
        songs = []
        for song_id in json_data:
            
            song_data = json_data[song_id]
            song = Song(**song_data)
            song.id = song_id
            songs.append(song)
        
        self.name = name
        self.songs = songs
        return self