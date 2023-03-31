![Repo Banner](https://user-images.githubusercontent.com/87353286/144381080-faf8e557-7909-43a1-a8e2-208936e5a8f8.png)

# BlackHole Playlists

BlackHole is an Open-Source Music Player App! It is able to stream from any server and thus reqiures no backend, it also supports streaming from YouTube and Spotify.

This is an example of how they structure the metadata for songs/playlists:

```
{
    "0zGcUoRlhmw": {
        "id": "0zGcUoRlhmw",
        "album": "ChainsmokersVEVO",
        "album_id": "UCRzzwLpLiUNIs6YOPe33eMg",
        "artist": "The Chainsmokers",
        "duration": "247",
        "genre": "YouTube",
        "has_lyrics": "false",
        "image": "https://img.youtube.com/vi/0zGcUoRlhmw/maxresdefault.jpg",
        "language": "YouTube",
        "release_date": "2016-10-24 00:00:00.000",
        "subtitle": "The Chainsmokers",
        "title": "Closer (Official Video) (feat. Halsey)",
        "url": "AUDIO_LINK_TEMP",
        "lowUrl": "LOW_URL",
        "highUrl": "HIGH_URL",
        "year": "2016",
        "320kbps": "false",
        "quality": null,
        "perma_url": "https://www.youtube.com/watch?v=0zGcUoRlhmw",
        "expire_at": "1680288169",
        "dateAdded": "2023-03-31 08:43:21.651723"
    }
}
```

based on this you can make a m3u like player.
