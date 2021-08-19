import pyautogui
import time
import logging
import asyncio
from colorama import *
from termcolor import colored, cprint
from ClassBot import classe

init(autoreset=True)  # Permette ad ogni print di ritornare al suo colore base
errore = colored("Please report this bug/error on github", 'red', attrs=['bold'])


def cimento(run):
    logging.debug("---------GAUNTLET----------")
    conta = 0
    logging.debug(f"run = {run}")
    cprint("\n-----GAUNTLET-----", 'cyan', attrs=['bold'])
    print(colored("run = ", 'green', attrs=['bold']), colored(run, 'white'))
    print(" ")
    if run <= 0:
        logging.debug("run <= 0")
        pyautogui.alert(text="Run must be > 0", button="OK")
        return 0
    else:
        # load-----------------------------
        auto = classe.bit(r"image\autored.png", 0.7)
        gaunt = classe.bit(r"image\cimento.png", 0.5)
        play = classe.bit(r"image\play.png", 0.4)
        accept = classe.bit(r"image\accept.png", 0.5)
        # ---------------------------------
        error = gaunt.bottone()
        if error == 0:
            cprint(errore)
            return 0
        while (True):
            conta += 1
            error = play.bottone()
            if error == 0:
                cprint(errore)
                return 0
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
            if conta == int(run):
                pyautogui.press('esc')
                time.sleep(3)
                pyautogui.press('esc')
                break
            else:
                pyautogui.press('esc')
                time.sleep(2)


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
