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
    logging.debug(f"run = {run}\n")
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
            # auto = classe.bit(r"image\autored.png", 0.7)
            gvg_button = classe.bit(r"image\gvg.png", 0.5)
            play = classe.bit(r"image\play.png", 0.5)
            select = classe.bit(r"image\battle2.png", 0.5)
            accept = classe.bit(r"image\accept.png", 0.5)
            # -------------------------------------
            error = gvg_button.bottone()
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
                '''
                error = auto.ispresence()
                if error == 0:
                    pyautogui.press('space')
                '''
                print("----------------------------------")
                print(f"run number: {conta}")
                asyncio.run(test())
                print("----------------------------------\n")
                time.sleep(2)
                pyautogui.press('esc')
                time.sleep(2)
                if conta == int(run):
                    pyautogui.press('esc')
                    break


async def fine():
    vittoria = classe.bit(r"image\cittadina.png", 0.5) # check red end button
    # sconfitta = classe.bit(r"image\sconfitta.png", 0.7) # Check Defeat screen
    while True:
        await asyncio.sleep(1)
        test = vittoria.SafeControl()
        if test == 1:
            return 1


async def test():
    prova = asyncio.create_task(fine())
    await prova
