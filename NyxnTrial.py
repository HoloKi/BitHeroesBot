import pyautogui
import time
import logging
from colorama import *
from termcolor import colored, cprint
import classe
import asyncio

init(autoreset=True)  # Permette ad ogni print di ritornare al suo colore base

errore = colored("Please report this bug/error on github or discord\n", 'red', attrs=['bold'])


def prove(run):
    print(colored("\n-----NYXN_TRIAL-----", 'cyan', attrs=['bold']))
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
            trial = classe.bit(r"image\prove.png", 0.5)
            play = classe.bit(r"image\play.png", 0.4)
            accept = classe.bit(r"image\accept.png", 0.5)
            yes = classe.bit(r"image\yes.png", 0.5)
            # -------------------------------------
            error = trial.bottone()
            if error == 0:
                cprint(errore)
                return 0
            while True:
                conta += 1
                error = play.bottone()
                if error == 0:
                    cprint(errore)
                    return 0
                error = accept.bottone()
                if error == 0:
                    cprint(errore)
                    return 0
                print("----------------------------------")
                print(f"run number: {conta}")
                asyncio.run(test())
                print("----------------------------------\n")
                error = yes.bottone()
                if error == 0:
                    cprint(errore)
                    return 0
                time.sleep(3)
                if conta == int(run):
                    pyautogui.press('esc')
                    break


async def fine():
    fine = classe.bit(r"image\fine.png", 0.7)
    morte = classe.bit(r"image\raid\raiddie.png", 0.7)
    while True:
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
