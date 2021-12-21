import os
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

# so basically what this script will do is
# convert mp4 files in the current directory
# into mp3 files
def main():
    # first we will get the directory
    print(f'INSIDE DIRECTORY: {os.listdir()}\n')
    
    # next we will loop through the directory
    # and search for mp4 files and append to entries[]
    entries = []
    for file in os.listdir():
        if str(file).endswith('.mp4'):
            print(f'FILE: {file}')
            entries.append(file)
        else:
            print(f'Nothing to append')

    for entry in entries:
        try:
            # we find the mp4 file
            mp4_file = os.path.abspath(entry)
            # we replace the mp4 with mp3
            mp3_file = os.path.abspath(str(entry).replace('mp4', 'mp3'))        
            # we set the video
            video = VideoFileClip(mp4_file, audio=True, fps_source='tbr')
            # we choose the audio
            audio = video.audio
            # we write to the mp3 file based on the variable - mp3_file
            audio.write_audiofile(mp3_file)
            # we close the audio and video
            audio.close()
            video.close()
        # if there is a KeyError as an exception
        # it probably means the mp4 has no video inside it
        # rather it just has audio
        except KeyError as ke:
            print(f'KeyError: {ke} => {entry}')
            # extract the audio from the mp4_file variable
            # then output it to the mp3_file variable
            try:
                ffmpeg_extract_audio(mp4_file, mp3_file)
                print(f'CONVERTED: "{mp4_file}" to .mp3')
                # remove the mp4_file from the directory
                os.remove(mp4_file)
                print(f'REMOVED: {mp4_file}')
                continue                
            except PermissionError as pe:
                print(pe)
                continue

main()
