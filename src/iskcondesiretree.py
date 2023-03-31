# %%
import os
from blackhole import Playlist, Song
from parse import parse_m3u, generate_json
from multiprocessing import Pool
import datetime
import subprocess

def parallel_get_url_data(urls):
    with Pool() as pool:
        results = []
        with tqdm(total=len(urls)) as pbar:
            for result in pool.imap_unordered(extract_url_data, urls):
                results.append(result)
                pbar.update()
        return results


def get_duration(url):
    duration = subprocess.check_output(f"ffmpeg -i {url} 2>&1 | grep 'Duration' | cut -d ' ' -f 4 | sed s/,//", shell=True)
    time_obj = datetime.datetime.strptime(str(duration.strip(), 'utf-8'), '%H:%M:%S.%f')
    seconds = (time_obj.hour * 60 * 60) + (time_obj.minute * 60) + time_obj.second + (time_obj.microsecond / 1000000)
    return seconds

def extract_url_data(url):
    # Example:
    # http://audio.iskcondesiretree.com:443/02_-_ISKCON_Swamis/ISKCON_Swamis_-_R_to_Y/His_Holiness_Radha_Govinda_Swami/00_-_Canto-Wise_Katha/01_-_Srimad_Bhagavatam_Katha/Canto-01/01_-_Saunakadi_Rishiyo_ke_Prasna-SB_01-01-02_-_2006_Kanpur/01_-_RGS_SB_01-01-01-03_Hindi_-_Saunakadi_Rishiyo_ke_Prasna-Day-01_-_2006-02-27_Kanpur.mp3

    url = url.replace(':443', '')
    url_parts = url.replace('_', ' ').split('/')
    album, title = url_parts[-2:]
    artist = url_parts[5]

    try:
        duration = str(int(get_duration(url)))
    except:
        print(f"Failed to get duration for {url}")
        duration = '0'

    return {'album': album, 'title': title, 'url': url, 'artist': artist, 'duration': duration}

if __name__ == "__main__":
    import argparse
    from tqdm import tqdm

    parser = argparse.ArgumentParser()
    parser.add_argument('--playlist', type=str, required=True)
    parser.add_argument('--name', type=str, required=True)
    parser.add_argument('--output', type=str, required=True)
    parser.add_argument('--image', type=str, required=False)

    args = parser.parse_args()

    urls = parse_m3u(args.playlist)
    data = parallel_get_url_data(urls)

    songs = []
    for row in tqdm(data):
        if row['url'].endswith('.mp3') == False:
            continue

        songs.append(Song(
            url = row['url'],
            perma_url = row['url'],
            title = row['title'],
            album = row['album'],
            artist = row['artist'],
            duration = row['duration'],
            image = args.image,
            subtitle = 'Lecture'
        ))
    
    # Create a playlist
    playlist = Playlist(name=args.name, songs=songs)
    playlist.createJSON(path=args.output)