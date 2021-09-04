import time
import multiprocessing
import concurrent.futures
import importlib
import asyncio
# importlib.import_module("playlocalsound")
from sub_modules import servermodulev2 as sm

def mpMethod():
    print("in main")
    beansProcess = multiprocessing.Process(target=pls.playLocalFile, args=["beans.mp3"])
    bestCryProcess = multiprocessing.Process(target=pls.playLocalFile, args=["bruh.mp3"])
    beansProcess.start()
    bestCryProcess.start()
    beansProcess.join()
    bestCryProcess.join()

def run_server():
    sm.run()

def main():
    # with concurrent.futures.ProcessPoolExecutor as executor:
    #     future1 = executor.submit(pls.playLocalFile, "bruh.mp3")
    #     print(future1.result())
    run_server()

if __name__ == "__main__":
    main()