import youtube_dl


def download_youtube_playlist(playlist_url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',
        'noplaylist': False,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])


if __name__ == '__main__':
    playlist_url = 'https://youtube.com/playlist?list=PL685s7vGIQZhOImb6BSxZsDFUeo-TDAdU'
    download_youtube_playlist(playlist_url)
    