# %%
import yt_dlp
from blackhole import Playlist, Song

# %%
def get_playlist_videos(playlist_url):
    ydl_opts = {
        "ignoreerrors": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        playlist_info = ydl.extract_info(playlist_url, download=False)
        songs = []

        try:
            for item in playlist_info['entries']:
                try:
                    for format in item['formats']:
                        if format['ext'] == 'm4a':
                            url = format['url']
                            continue

                    song = Song(
                        id=item['id'],
                        album=playlist_info['title'],
                        album_id=playlist_info['id'],
                        artist=item['uploader'],
                        genre='YouTube',
                        title=item['title'],
                        image=item['thumbnails'][0]['url'],
                        language='YouTube',
                        subtitle='YouTube',
                        perma_url=item['webpage_url'],
                        duration=item['duration'],
                        url = url,
                        expire_at = "1680088169")
                    songs.append(song)
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
        return songs 

# %%
if "__main__" == __name__:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="Youtube playlist url", required=True)
    parser.add_argument('--name', type=str, required=True)
    parser.add_argument('--output', type=str, required=True)

    args = parser.parse_args()

    songs = get_playlist_videos(args.url)

    playlist = Playlist(name=args.name, songs=songs)
    playlist.createJSON(path=args.output)
