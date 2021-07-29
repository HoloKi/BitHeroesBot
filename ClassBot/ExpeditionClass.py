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
    count = 0
    logging.debug(f"run = {run}")
    cprint("\n-----EXPEDITION-----", 'cyan', attrs=['bold'])
    print(colored("run = ", 'green', attrs=['bold']), colored(run, 'white'))
    if run <= 0:
        logging.debug("run <= 0")
        pyautogui.alert(text="Run must be > 0", button="OK")
        exit(0)
    else:
        #load_class-------------------------
        expe = classe.bit(r"image\entra.png", 0.5)
        accept = classe.bit(r"image\accept.png", 0.5)
        xbutt = classe.bit(r"image\xbutton.png", 0.5)
        yes = classe.bit(r"image\yes.png", 0.5)
        #----------------------------------
        while(True):
            count += 1
            error = expe.bottone()
            if error == 0:
                cprint(errore)
                return 0
            error = accept.bottone()
            if error == 0:
                cprint(errore)
                return 0
            print("----------------------------------")
            print(f"Match n: {count}")
            asyncio.run(test())
            print("----------------------------------\n")
            error = yes.bottone()
            if error == 0:
                cprint(errore)
                return 0
            time.sleep(3)
            if count == int(run):
                error = xbutt.bottone()
                if error == 0:
                    cprint(errore)
                    return 0
                pyautogui.press('esc')
                time.sleep(2)
                pyautogui.press('esc')
                break


async def fine():
    fine = classe.bit(r"image\fine.png", 0.7)
    morte = classe.bit(r"image\raid\raiddie.png", 0.7)
    while(True):
        await asyncio.sleep(1)
        test = morte.ispresence()
        if test == 1:
            return 2
        test = fine.ispresence()
        if test == 1:
            return 1

async def test():
    prova = asyncio.create_task(fine())
    await prova