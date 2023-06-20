import youtube
import concurrent.futures


youtube_playlists = {
    "YUGA-DHARMA HARINAM SANKIRTAN": "https://www.youtube.com/playlist?list=PLmkX1ry97x0y341HeBHxxo2dMl54Y3Twh",
    "Carana Sevane": "https://www.youtube.com/playlist?list=PLmkX1ry97x0zQP6zsdzzpGriSpxMFCQbU",
    "Bhakata Vatsala": "https://www.youtube.com/playlist?list=PLmkX1ry97x0zOhpoBOAPNPf-PKZ-buX6",
    "Kevala Kṛṣṇa Sukha": "https://www.youtube.com/playlist?list=PLmkX1ry97x0yPYBOTBnxeIzuO_JKK_yLO",
    "Krishna Dasa Babaji Maharaja": "https://www.youtube.com/playlist?list=PLhjoxAq83qqwSnaFYp0jW45tg0uvxbNuA"
}

for name, url in youtube_playlists.items():
    songs = youtube.get_playlist_videos(url)
    playlist = youtube.Playlist(name=name, songs=songs)
    playlist.createJSON(path='.')