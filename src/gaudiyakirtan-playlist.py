# %%
import os
from blackhole import Playlist, Song
import pandas as pd
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from iskcondesiretree import get_duration
from tqdm import tqdm

# Path to directory containing MP3 files
mp3_dir = '/Users/kendreaditya/Documents/workspace/media-files/gaudiyakirtan/audio/'

# Create an empty list to store the extracted data
data = []

get_tag = lambda tags, key: tags[key][0] if key in tags else None
get_url = lambda filename: 'https://gaudiyakirtan.s3.amazonaws.com/audio/' + filename.split('/')[-1]

# Loop through all the files in the directory
for filename in tqdm(os.listdir(mp3_dir)):
    if filename.endswith('.mp3'):
        # Load the tags for the file using Mutagen
        tags = EasyID3(os.path.join(mp3_dir, filename))
        
        # Extract the relevant data from the tags
        title = get_tag(tags, 'title')
        artist = get_tag(tags, 'artist')
        album = get_tag(tags, 'album')

        audio = MP3(os.path.join(mp3_dir, filename))
        duration = str(int(get_duration(get_url(filename))))
        
        # Append the data to the list
        data.append({'url': get_url(filename), 'filename': filename, 'title': title, 'artist': artist, 'album': album, 'duration': duration})

# %%

# Create a DataFrame from the extracted data
df = pd.DataFrame(data)

# Create map of album to image URL
songs = []
for _, row in df.iterrows():
    
    songs.append(Song(
        url = row['url'],
        perma_url = row['url'],
        title = row['title'],
        album = row['album'],
        artist = row['artist'],
        duration = row['duration'],
        image = "https://www.iskconbangalore.org/blog/wp-content/uploads/2020/03/Pastimes-of-Chaitanya-Mahaprabhu.jpg",
        subtitle = 'Kirtan'
    ))

# Create a playlist
playlist = Playlist(name='Gaudiya Kirtan', songs=songs)
playlist.createJSON(path='./../playlists/')

# %%
