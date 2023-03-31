import argparse
import os
import re
import json
from urllib.parse import urlparse


def parse_m3u(m3u_file):
    """
    Parse the m3u file and return a list of URLs for each track.
    """
    urls = []
    with open(m3u_file, "r") as f:
        for line in f:
            # Ignore comments and blank lines
            if line.startswith("#") or not line.strip():
                continue
            urls.append(line.strip())
    return urls


def parse_url(url):
    """
    Parse the URL and extract information about the track.
    """
    parsed_url = urlparse(url)
    track_id = os.path.splitext(os.path.basename(parsed_url.path))[0]
    return {
        "id": track_id,
        "album": "",
        "album_id": "",
        "artist": "",
        "duration": "",
        "genre": "",
        "has_lyrics": "",
        "image": "",
        "language": "",
        "release_date": "",
        "subtitle": "",
        "title": track_id,
        "url": url,
        "lowUrl": url
    }


def generate_json(urls, output_dir):
    """
    Generate a JSON file for each mp3 track in the m3u file.
    """
    for url in urls:
        if not url.endswith(".mp3"):
            continue
        track_data = parse_url(url)
        output_file = os.path.join(output_dir, f"{track_data['id']}.json")
        with open(output_file, "w") as f:
            json.dump({track_data['id']: track_data}, f, indent=4)
        print(f"Generated {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate JSON files for each mp3 track in an m3u file.")
    parser.add_argument("m3u_file", help="The m3u file to process")
    parser.add_argument("-o", "--output-dir", help="The directory to output the JSON files to", default=".")
    args = parser.parse_args()

    if not os.path.isfile(args.m3u_file):
        print(f"Error: {args.m3u_file} is not a file.")
        exit(1)

    if not os.path.isdir(args.output_dir):
        print(f"Error: {args.output_dir} is not a directory.")
        exit(1)

    urls = parse_m3u(args.m3u_file)
    generate_json(urls, args.output_dir)
