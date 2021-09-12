import pyautogui
import time
import logging
from colorama import *
from termcolor import colored, cprint
from ClassBot import classe
import asyncio

init(autoreset=True)  # Permette ad ogni print di ritornare al suo colore base

errore = colored("Please report this bug/error on github or discord\n", 'red', attrs=['bold'])


def invasione(run):
    logging.debug("---------INVASION----------")
    print(colored("\n-----INVASION-----", 'cyan', attrs=['bold']))
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
            trial = classe.bit(r"image\invasione.png", 0.5)
            play = classe.bit(r"image\play.png", 0.4)
            accept = classe.bit(r"image\accept.png", 0.5)
            no_shard = classe.bit(r"image\noshard.png", 0.5)
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
                # check if no shard is presence
                error = no_shard.SafeControl()
                if error == 1:
                    logging.debug("No shard available!")
                    pyautogui.press("esc")
                    time.sleep(2)
                    pyautogui.press("esc")
                    return 0
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
                time.sleep(3)
                if conta == int(run):
                    pyautogui.press('esc')
                    break


async def fine():
    end = classe.bit(r"image\cittadina.png", 0.5)
    while True:
        await asyncio.sleep(1)
        prova = end.SafeControl()
        if prova == 1:
            return 1


async def test():
    prova = asyncio.create_task(fine())
    await prova
