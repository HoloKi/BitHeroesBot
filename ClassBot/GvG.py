import pyautogui
import time
import logging
from colorama import *
from termcolor import colored, cprint
from ClassBot import classe
import asyncio

init(autoreset=True)  # Permette ad ogni print di ritornare al suo colore base

errore = colored("Please report this bug/error on github or discord\n", 'red', attrs=['bold'])


def gvg(run):
    logging.debug("---------GVG----------")
    print(colored("\n-----GVG-----", 'cyan', attrs=['bold']))
    print(colored("run = ", 'green', attrs=['bold']), colored(run, 'white'))
    conta = 0
    logging.debug(f"run = {run}")
    if run < 0:
        logging.debug("Run < 0")
        pyautogui.alert(text="Run must be > 0", button="OK")
        return 0
    else:
        if run == 0:
            print(colored("Skip Prove di Nyxn", 'red', attrs=['bold']))
            return 0
        else:
            # load_class---------------------------
            auto = classe.bit(r"image\autored.png", 0.7)
            gvg = classe.bit(r"image\gvg.png", 0.5)
            play = classe.bit(r"image\play.png", 0.5)
            select = classe.bit(r"image\battle2.png", 0.5)
            accept = classe.bit(r"image\accept.png", 0.5)
            yes = classe.bit(r"image\yes.png", 0.5)
            # -------------------------------------
            error = gvg.bottone()
            if error == 0:
                cprint(errore)
                return 0
            while True:
                error = play.bottone()
                if error == 0:
                    cprint(errore)
                    return 0
                error = select.bottone()
                if error == 0:
                    cprint(errore)
                    return 0
                conta += 1
                error = accept.bottone()
                if error == 0:
                    cprint(errore)
                    return 0
                error = auto.ispresence()
                if error == 0:
                    pyautogui.press('space')
                print("----------------------------------")
                print(f"run number: {conta}")
                asyncio.run(test())
                print("----------------------------------\n")
                error = yes.bottone()
                if error == 0:
                    cprint(errore)
                    return 0
                time.sleep(2)
                if conta == int(run):
                    pyautogui.press('esc')
                    break


async def fine():
    vittoria = classe.bit(r"image\gvgvict.png", 0.7)
    sconfitta = classe.bit(r"image\endinv.png", 0.7)
    while (True):
        await asyncio.sleep(1)
        test = vittoria.ispresence()
        if test == 1:
            return 2
        test = sconfitta.ispresence()
        if test == 1:
            return 1


async def test():
    prova = asyncio.create_task(fine())
    await prova
