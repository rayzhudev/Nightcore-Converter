import sys, os, librosa, math
from moviepy.editor import *
# from moviepy.audio import *
folder = sys.argv[1]
try: 
    os.chdir(folder)
    for filename in os.listdir(folder):
        if filename.endswith(".mp3") and not os.path.isfile("../nightcored songs/" + filename):
            #speed song up by root 2
            audio = AudioFileClip(filename)
            nightcore_audio = audio.fx(vfx.speedx, math.sqrt(2))
            nightcore_audio.write_audiofile("../nightcored songs/" + filename)
        os.remove(filename)
except Exception as e:
    print(e)
    exit
