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
        for item in playlist_info['entries']:
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
                url = "https://rr2---sn-8xgp1vo-2iay.googlevideo.com/videoplayback?expire=1680088169&ei=SdUmZPvwAdHT8wS2pauoDw&ip=173.67.178.225&id=o-APY4rpz1BdCq351Qvsc0h5yjhr3TCb-SAh2EZ1Bw6_Lu&itag=140&source=youtube&requiressl=yes&mh=jl&mm=31%2C29&mn=sn-8xgp1vo-2iay%2Csn-ab5l6nrz&ms=au%2Crdu&mv=m&mvi=2&pl=18&gcr=us&initcwndbps=1620000&vprv=1&mime=audio%2Fmp4&gir=yes&clen=3997587&dur=246.967&lmt=1663920603783549&mt=1680266246&fvip=3&keepalive=yes&fexp=24007246&beids=24512778&c=ANDROID&txp=5532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAN9eZtKrx8pS1mFKVSpV5upnW56up_e2mypDAkAT-OxcAiBpcM25c0XonpnNLOA3EzpMbGtYe46SHGVU8UYRb7HOvQ%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgbmzJGwcHDb2F8lGEI34Fr3n4CuyplGWtjd3Juj527VcCIQC25wK7vOexNEMQQnrt5B74EvXzvxFbpeHulfuPxurPfw%3D%3D",
                expire_at = "1680088169")
            songs.append(song)
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
