from pytubefix import YouTube

def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    print(f"Status: {round(pct_completed, 2)} %")


download_directory = './download/'
url = str(input('Bitte Youtube-URL angeben: '))

yt = YouTube(url, on_progress_callback=on_progress)
ys = yt.streams.get_audio_only()

out = ys.download(output_path=download_directory)

print(f"Download complete: {out}")
