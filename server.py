import time
import multiprocessing
import concurrent.futures
import importlib
# importlib.import_module("playlocalsound")
from sub_modules import playlocalsound as pls

def mpMethod():
    print("in main")
    # beansProcess = multiprocessing.Process(target=pls.play, args=["beans.mp3"])
    bestCryProcess = multiprocessing.Process(target=pls.playLocalFile, args=["bruh.mp3"])
    # beansProcess.start()
    bestCryProcess.start()
    # beansProcess.join()
    bestCryProcess.join()


def main():
    with concurrent.futures.ProcessPoolExecutor as exexutor:
        future1 = exexutor.submit(pls.playLocalFile, "bruh.mp3")


if __name__ == "__main__":
    main()