import os, glob, shutil

directoryEntrys = glob.glob('./music/*.mp3')

for files in directoryEntrys:
  shutil.move(files, os.path.expanduser('~') + '/Musik')
  
  