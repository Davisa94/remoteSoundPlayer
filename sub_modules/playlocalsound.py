from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
import os
import pygame
import vlc


# given the filename return the appropriate path:
def filenameToPath(filename):
    # Get current directory
    cwd = os.getcwd()
    # Go up a folder
    cwd = cwd.split("\sub_modules")
    cwd = cwd[0]
    # Convert backslashes to forward slashes
    cwd = cwd.replace("\\", "/")
    # append the filename onto the path and print that it is playing
    finalPath = f"{cwd}/{filename}"
    print( f"Now playing: {finalPath}")
    return finalPath
    # return filename

def getCWD():
    # Get current directory
    cwd = os.getcwd()
    # Go up a folder
    cwd = cwd.split("\sub_modules")
    cwd = cwd[0]
    # Convert backslashes to forward slashes
    cwd = cwd.replace("\\", "/")
    return cwd

def playLocalFilePyDub(filename):
    path = filenameToPath(filename)
    song = AudioSegment.from_mp3(path)
    song.export(getCWD(), form)
    play(song)

def playLocalFileVlc(filename):
    path = filenameToPath(filename)
    song = vlc.MediaPlayer(path)
    song.play()

def playLocalFilePyGame(filename):
    path = filenameToPath(filename)
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

def playLocalFile(filename):
    path = filenameToPath(filename)
    # sound = AudioSegment.from_mp3(path)
    playsound(path)
    # play(sound)
    return f"Finished playing {path}"
def playLocalFileSystem(filename):
    path = filenameToPath(filename)
    os.system(path)
# TODO: add a loop that tries to play the filename without extension given an extensionless filename
playLocalFileVlc("bestcrie.mp3")