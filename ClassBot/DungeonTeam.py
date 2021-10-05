import pyautogui
import time
import logging
from colorama import *
from termcolor import colored, cprint
from ClassBot import classe
import asyncio

init(autoreset=True)  # Permette ad ogni print di ritornare al suo colore base

errore = colored("Please report this bug/error on github or discord\n", 'red', attrs=['bold'])


"""
Dungeon function that uses the class to simplify the code and its reuse
@: param run = number of runs that the player does (assumes it is already int)
@: param difficult = level difficulty (assumes it is already a string from the menu)
@: param duration = time in seconds to complete the run (assumes it is already int)
@: return 1 if everything went well
@: return 0 if it went wrong
"""


def dungeonteam(run):
    logging.debug("---------DUNGEON----------")
    count = 0
    # LOAD CLASS FIRST-----------------------------------------------------------------
    accetta = classe.bit(r"image\accept.png", 0.5)
    cittadina = classe.bit(r"image\cittadina.png", 0.5)
    chiudi = classe.bit(r"image\raid\close.png", 0.5)
    morte = classe.bit(r"image\raid\raiddie.png", 0.7)
    #fine = classe.bit(r"image\rerun.png", 0.5)
    rerun = classe.bit(r"image\rerun.png", 0.5)
    # ---------------------------------------------------------------------------------
    print(colored("\n-----DUNGEON-----", 'cyan', attrs=['bold']))
    print(colored("run = ", 'green', attrs=['bold']), colored(run, 'white'),
          colored(" difficult = ", 'green', attrs=['bold']))
    print(" ")
    logging.debug(f"run = {run}")
    # caso in cui le run sono minori di 0, ritorna 0
    if int(run) <= 0:
        logging.debug("run < 0")
        pyautogui.alert(text='the number of raid runs must be 1 or greater', button='OK')
        return 0
    else:
        # Caso in cui non voglio fare raid RUN=0, ritorna 0
        if int(run) == 0:
            logging.debug("run=0")
            return 0
        else:
            error = accetta.bottone()
            if error == 0:
                cprint(errore)
                return 0
            while True:
                count += 1
                print("----------------------------------")
                print(f"run number: {count}")
                asyncio.run(test())
                # controllo se è morto---------------
                error = morte.ispresence()
                if error == 1:  # se è morto clicca
                    chiudi.bottone()
                    print("your team is dead!")
                    print("----------------------------------\n")
                    time.sleep(5)
                    pyautogui.press('esc')
                    break
                print("----------------------------------\n")
                if int(count) == int(run):
                    logging.debug("end")
                    time.sleep(3)
                    pyautogui.press('esc')
                    time.sleep(3)
                    pyautogui.press('esc')
                    break
                else:
                    error = rerun.bottone()
                    if error == 0:
                        cprint(errore)
                        return 0
                    time.sleep(3)
        return 0

async def fine():
    fine = classe.bit(r"image\fine.png", 0.7)
    morte = classe.bit(r"image\raid\raiddie.png", 0.7)
    while True:
        await asyncio.sleep(1)
        test = morte.SafeControl()
        if test == 1:
            return 2
        test = fine.SafeControl()
        if test == 1:
            return 1

async def test():
    prova = asyncio.create_task(fine())
    await prova