from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
import os


# given the filename return the appropriate path:
def filenameToPath(filename):
    cwd = os.getcwd()
    print(cwd)
    cwd = cwd.split("\sub_modules")
    cwd = cwd[0]
    cwd = cwd.replace("\\", "/")
    print( f"{cwd}/{filename}")
    return f"{cwd}/{filename}"
    # return filename


def playLocalFile(filename):
    path = filenameToPath(filename)
    # sound = AudioSegment.from_mp3(path)
    playsound(path)
    # play(sound)

playLocalFile("bestcrie.mp3")
# TODO: add a loop that tries to play the filename without extension given an extensionless filename