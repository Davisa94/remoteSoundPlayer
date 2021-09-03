from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play


# given the filename return the appropriate path:
def filenameToPath(filename):
    return f"../{filename}"


def playLocalFile(filename):
    path = filenameToPath(filename)
    sound = AudioSegment.from_mp3(path)
    playsound(path)

play("bestcry.mp3")
# TODO: add a loop that tries to play the filename without extension given an extensionless filename