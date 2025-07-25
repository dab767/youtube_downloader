from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

import glob

directoryContent = glob.glob('./music/*.mp3')

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
    