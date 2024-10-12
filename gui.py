import tkinter
import customtkinter
from pytubefix import YouTube

def startDownload():
  try:
    finishLabel.configure(text='')
    
    youtube_link = link.get()
    youtube_obj = YouTube(youtube_link, on_progress_callback=on_progress)
    
    audio = youtube_obj.streams.get_audio_only()
    audio.download(output_path='./download/')
    
    finishLabel.configure(text="Download complete")
  except:
    finishLabel.configure(text='Youtube link is invalid', text_color='red')
  

def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    #print(f"Status: {round(pct_completed, 2)} %")
    percent = str(int(pct_completed))
    pPercentage.configure(text=percent + '%')
    pPercentage.update()
    
    progressBar.set(float(pct_completed) / 100)

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('green')

app = customtkinter.CTk()
app.geometry('720x480')
app.title('Youtube to MP3 converter')

title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

finishLabel = customtkinter.CTkLabel(app, text='')
finishLabel.pack()

pPercentage = customtkinter.CTkLabel(app, text='0%')
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

download = customtkinter.CTkButton(app, text='Convert', command=startDownload)
download.pack(padx=10, pady=10)

app.mainloop()