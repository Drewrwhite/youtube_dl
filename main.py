import os
from pytube import Playlist
from pytube.exceptions import AgeRestrictedError


def download_youtube_playlist(playlist_url):
    playlist = Playlist(playlist_url)
    playlist_name = playlist.title

    parent_folder = os.path.join(os.getcwd(), 'data')
    os.makedirs(parent_folder, exist_ok=True)

    output_folder = os.path.join(parent_folder, playlist_name)
    os.makedirs(output_folder, exist_ok=True)

    for video in playlist.videos:
        try:
            video.streams.get_highest_resolution().download(output_path=output_folder)
        except Exception as e:
            print(f"Error occurred for video: {video.title}")
            print(f"Error message: {str(e)}")
            continue


if __name__ == '__main__':
    playlist_url = 'https://youtube.com/playlist?list=PL685s7vGIQZhOImb6BSxZsDFUeo-TDAdU'
    download_youtube_playlist(playlist_url)
