from playsound import playsound


# given the filename return the appropriate path:
def filenameToPath(filename):
    return f"../{filename}"


def play(filename):
    path = filenameToPath(filename)
    playsound(path)


# TODO: add a loop that tries to play the filename without extension given an extensionless filename