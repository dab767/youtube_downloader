from pytubefix import YouTube
import os

def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    print(f"Status: {round(pct_completed, 2)} %")

if not os.path.exists('./download'):
    os.mkdir('./download')

download_directory = './download/'
url = str(input('Bitte Youtube-URL angeben: '))

yt = YouTube(url, 'WEB', on_progress_callback=on_progress);

print(yt.title);

ys = yt.streams.get_audio_only()

out = ys.download(output_path=download_directory)

print(f"Download complete: {out}")
