import json
import logging
from ClassBot import Menu, checkers
from colorama import *
import os.path

init(autoreset=True)

VERSION = "5.5.2"


'''
Function to resize bot window
'''
from ctypes import windll, byref
import ctypes.wintypes as wintypes

STDOUT = -11

hdl = windll.kernel32.GetStdHandle(STDOUT)
rect = wintypes.SMALL_RECT(0, 0, 56, 26)  # (left, top, right, bottom)
windll.kernel32.SetConsoleWindowInfo(hdl, True, byref(rect))



def main():
    logging.basicConfig(filename="latest.log", filemode="w", format='%(asctime)s - %(funcName)s :   %(message)s',
                        level=logging.DEBUG)
    logging.info(f"VERSION : {VERSION} - BOT by HoloKi. Info : https://github.com/HoloKi/BitHeroesBot")
    logging.info("https://discord.gg/h98xsssEpe")
    logging.info(
        "The bot is completely free, any sale is prohibited.If someone sold it to you, get your money back and report it to the developer")
    print(f"BitHeroesBot by Holoki ------ VERSION = {VERSION} ------")
    print("Translate by PastShadie")
    print("All info on latest.log")
    # check if there isnt a data.json
    file = os.path.isfile("data.json")
    logging.debug(f"data.json = {file}")
    if file is False:
        f = open("data.json", "x")
        data_dict = {"name": checkers.USER, "raid": "0", "difficulty": "heroic", "pvp": "0", "gauntlet": "0", "yes": "0"}
        json.dump(data_dict, f)
        f.close()
        # time.sleep(3)
    #checkers.check()
    while True:
        cycle = Menu.menu()
        if cycle == 0:
            exit()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.error(e)
