import sys, os, librosa, math, eyed3
from moviepy.editor import *

folder = sys.argv[1]
try: 
    os.chdir(folder)
    for filename in os.listdir(folder):
        if filename.endswith(".mp3") and not os.path.isfile("../nightcored songs/" + filename):
            #speed song up by root 2
            audio = AudioFileClip(filename)
            nightcore_audio = audio.fx(vfx.speedx, math.sqrt(2))
            nightcore_audio.write_audiofile("../nightcored songs/" + filename)
            song = eyed3.load("../nightcored songs/" + filename)
            song.tag.artist = filename.split(" - ")[0]
            song.tag.title = filename.split(" - ")[1][:-4]
            song.tag.album_artist = song.tag.artist
            song.tag.save()
        elif filename.endswith(".mp3"):
            os.remove(filename) #comment out this section to not delete the file after converting
except Exception as e:
    print(e)
    exit
