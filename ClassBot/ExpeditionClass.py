import pyautogui
import time
import asyncio
import logging
from colorama import *
from termcolor import colored,cprint
from ClassBot import classe

init(autoreset=True)  # Permette ad ogni print di ritornare al suo colore base


errore = colored("Please report this bug/error on github",'red',attrs=['bold'])


def expedition(run):
    logging.debug("---------EXPEDITION----------")
    count = 0
    logging.debug(f"run = {run}")
    cprint("\n-----EXPEDITION-----", 'cyan', attrs=['bold'])
    print(colored("run = ", 'green', attrs=['bold']), colored(run, 'white'))
    if run <= 0:
        logging.debug("run <= 0")
        pyautogui.alert(text="Run must be > 0", button="OK")
        exit(0)
    else:
        # load_class-------------------------
        enter = classe.bit(r"image\entra.png", 0.5)
        accept = classe.bit(r"image\accept.png", 0.6)
        cittadina =  classe.bit(r"image\cittadina.png",0.5)
        # ----------------------------------
        while True:
            count += 1
            error = enter.bottone()
            if error == 0:
                cprint(errore)
                return 0
            enter.ispresence()
            error = accept.bottone()
            if error == 0:
                cprint(errore)
                return 0
            accept.ispresence()
            print("----------------------------------")
            print(f"Match n: {count}")
            asyncio.run(test())
            print("----------------------------------\n")
            time.sleep(3)
            error = cittadina.bottone()
            if error == 0:
                cprint(errore)
                return 0
            cittadina.ispresence()
            if count == int(run):
                pyautogui.press('esc')
                logging.debug("esc 2 count==run ")
                time.sleep(3)
                pyautogui.press('esc')
                logging.debug("esc 3")
                time.sleep(3)
                pyautogui.press('esc')
                logging.debug("esc 4")
                time.sleep(3)
                break


async def fine():
    fine = classe.bit(r"image\cittadina.png", 0.7)
    while True:
        await asyncio.sleep(1)
        test = fine.SafeControl()
        if test == 1:
            return 1

async def test():
    prova = asyncio.create_task(fine())
    await prova
