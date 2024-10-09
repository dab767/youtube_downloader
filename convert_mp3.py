import os, subprocess, glob

downloadDirectory = './download/'
musicDirectory = './music/'


def convert_video_to_mp3(input_file, output_file):
    ffmpeg_cmd = [
        'ffmpeg',
        '-i', input_file,
        '-vn',
        '-acodec', 'libmp3lame',
        '-ab', '128k',
        '-ar', '44100',
        '-y',
        output_file
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print('Successfully converted!')
    except subprocess.CalledProcessError as e:
        print('Conversion failed!')

directory_content = glob.glob(downloadDirectory+'*.*')

for files in directory_content:
    fileNames = files.split('/')[2]
    base, ext = fileNames.split('.')

    convert_video_to_mp3(downloadDirectory + fileNames, musicDirectory + base + '.mp3')

    os.remove(files)

