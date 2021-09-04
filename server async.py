import time
import multiprocessing
import concurrent.futures
import importlib
import asyncio
# importlib.import_module("playlocalsound")
from sub_modules import servermodulev2 as sm


def run_server():
    sm.run()

def main():
    run_server()

if __name__ == "__main__":
    main()