import threading
import requests
import os
import blackhole

class Downloader(threading.Thread):
    def __init__(self, playlist_name, song):
        super().__init__()
        self.playlist_name = playlist_name
        self.song = song

    def run(self):
        url = self.song.url
        file_name = f"{self.song.id}.m4a"
        folder_path = os.path.join(self.playlist_name, '')

        # Create the playlist folder if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)

        file_path = os.path.join(folder_path, file_name)

        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)
        else:
            print(f"Failed to download {file_name}")


if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser()
    parser.add_argument("--playlist", help="Playlist path", required=True)
    args = parser.parse_args()
    playlist_path = args.playlist

    playlist = blackhole.Playlist()
    playlist_json = json.load(open(playlist_path, 'r'))
    playlist.load(playlist_json, playlist_path.split('/')[-1].split('.')[0])

    threads = []
    for song in playlist.songs:
        thread = Downloader(playlist.name, song)
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("All downloads completed.")
