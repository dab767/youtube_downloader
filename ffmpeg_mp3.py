import os, subprocess, glob
import ffmpeg

if not os.path.exists('./music'):
    os.mkdir('./music')
    
downloadDirectory = './download/'
musicDirectory = './music/'

directory_content = glob.glob(downloadDirectory+'*.*')

for files in directory_content:
    fileNames = files.split('/')[2]
    base, ext = fileNames.split('.')
    
    inputFile = (f"{base}.{ext}")
    outputFile = (f"{base}.mp3")
    
    print(inputFile)

    """
    (
      ffmpeg.input(inputFile).output(outputFile).run()
    )
    """