from playsound import playsound


# given the filename return the appropriate path:
def filenameToPath(filename):
    return f"../{filename}"


def play(filename):
    playsound(filename)



play("../beans.mp3")