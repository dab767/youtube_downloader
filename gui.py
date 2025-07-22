import tkinter
import customtkinter
from pytubefix import YouTube
import os, subprocess, glob, shutil
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

if not os.path.exists('./music'):
    os.mkdir('./music')

if not os.path.exists('./download'):
    os.mkdir('./download')
  
downloadDirectory = './download/'
musicDirectory = './music/'

def moveMP3toUserDir(directory):
    directoryEntrys = glob.glob(f'{directory}/*.mp3')

    for files in directoryEntrys:
        shutil.move(files, os.path.expanduser('~') + '/Musik')

def mp3Tag(directory):
    directoryContent = glob.glob(f"{directory}*.mp3")
    
    try:
        for files in directoryContent:
            fileName = files.split('/')[2]
    
            mp3Tag = MP3(files, ID3=EasyID3)    
            
            if(len(fileName.split('-')) == 2):
                artist, title = fileName.split('-')
                mp3Tag['title'] = [title.split('.')[0]]
                mp3Tag['artist'] = [artist]
                mp3Tag.save()
            else:
                title = fileName.split('.')
                mp3Tag['title'] = title[0]
                mp3Tag.save()
            
            return True
    except:
        return False

def convert_video_to_mp3(input_file, output_file):
    ffmpeg_cmd = ['ffmpeg','-i', input_file,'-vn','-acodec', 'libmp3lame','-ab', '192k','-ar', '44100','-y',output_file]
    
    try:
        return_code = subprocess.run(ffmpeg_cmd, check=True)
        os.remove(input_file)
        
        print('Successfully converted!')
        return True
    except subprocess.CalledProcessError as e:
        print('Conversion failed!')
        return False


def download_convert():
  try:
    finishLabel.configure(text='')
    
    youtube_link = link.get()
    youtube_obj = YouTube(youtube_link, 'WEB', on_progress_callback=on_progress)
    
          
    audio = youtube_obj.streams.get_audio_only()
    filepath = audio.download(output_path='./download/')
    file_tmp = filepath.split("/")
    filename = file_tmp[-1]
    base, ext = filename.split(".")
    
    if convert_video_to_mp3(filepath, f"./music/{base}.mp3"):        
        mp3Tag(musicDirectory)        
        finishLabel.configure(text="Download and converting complete")
        
        
    moveMP3toUserDir(musicDirectory)
  except:
    finishLabel.configure(text='Youtube link is invalid', text_color='red')
    

def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    print(f"Status: {round(pct_completed, 2)} %")
    percent = str(int(pct_completed))
    pPercentage.configure(text=percent + '%')
    pPercentage.update()
    
    progressBar.set(float(pct_completed) / 100)

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('green')

app = customtkinter.CTk()
#app.geometry('720x480')
app.title('Youtube to MP3 converter')

title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.focus()
link.pack()

finishLabel = customtkinter.CTkLabel(app, text='')
finishLabel.pack()

pPercentage = customtkinter.CTkLabel(app, text='0%')
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

download = customtkinter.CTkButton(app, text='Download & Convert', command=download_convert)
download.pack(padx=10, pady=10)

app.mainloop()