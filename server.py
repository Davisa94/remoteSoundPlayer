import time
import multiprocessing
import importlib
# importlib.import_module("playlocalsound")
from sub_modules import playlocalsound as pls



def main():
    print("in main")
    # beansProcess = multiprocessing.Process(target=pls.play, args=["beans.mp3"])
    bestCryProcess = multiprocessing.Process(target=pls.playLocalFile, args=["bestcry.mp3"])
    # beansProcess.start()
    bestCryProcess.start()
    # beansProcess.join()
    bestCryProcess.join()



if __name__ == "__main__":
    main()