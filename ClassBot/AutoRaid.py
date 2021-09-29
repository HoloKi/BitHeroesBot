import pyautogui
import time
import logging
from colorama import *
from termcolor import colored, cprint
from ClassBot import classe
import asyncio
import json

init(autoreset=True)  # Permette ad ogni print di ritornare al suo colore base

errore = colored("Please report this bug/error on github or discord\n", 'red', attrs=['bold'])
"""
Raid function that uses the class to simplify the code and its reuse
@: param run = number of runs that the player does (assumes it is already int)
@: param difficult = level difficulty (assumes it is already a string from the menu)
@: param duration = time in seconds to complete the run (assumes it is already int)
@: return 1 if everything went well
@: return 0 if it went wrong
"""

f = open("data.json","r")
data = json.loads(f.read())

raid_data = float(data['Function'][0]['raid'][0]['raid'])
evoca_data = float(data['Function'][0]['raid'][0]['evoca'])
accetta_data = float(data['Function'][0]['raid'][0]['accept'])
chiudi_data = float(data['Function'][0]['raid'][0]['chiudi'])
morte_data = float(data['Function'][0]['raid'][0]['morte'])
rerun_data = float(data['Function'][0]['raid'][0]['rerun'])
no_shard_data = float(data['Function'][0]['raid'][0]['no_shard'])



def raid(run, difficult):
    logging.debug("---------RAID----------")
    hero = "heroic"
    hard = "hard"
    norm = "normal"
    difficulty = None  # default
    count = 0
    # LOAD CLASS FIRST-----------------------------------------------------------------
    if difficult == hero:
        difficulty = classe.bit(r"image\raid\heroic.png", 0.7)
    else:
        if difficult == hard:
            difficulty = classe.bit(r"image\raid\hard.png", 0.7)
        else:
            if difficult == norm:
                difficulty = classe.bit(r"image\raid\normal.png", 0.7)

    # auto = classe.bit(r"image\autogreen.png", 0.7)
    raid = classe.bit(r"image\raid\raid.png", raid_data)
    evoca = classe.bit(r"image\startraid.png", evoca_data)
    accetta = classe.bit(r"image\accept.png", accetta_data)
    chiudi = classe.bit(r"image\raid\close.png", chiudi_data)
    morte = classe.bit(r"image\raid\raiddie.png", morte_data)
    rerun = classe.bit(r"image\rerun.png", rerun_data)
    no_shard = classe.bit(r"image\noshard.png", no_shard_data)
    # ---------------------------------------------------------------------------------
    logging.debug(f"difficult = {difficulty.getImage()}.")
    print(colored("\n-----RAID-----", 'cyan', attrs=['bold']))
    print(colored("run = ", 'green', attrs=['bold']), colored(run, 'white'),
          colored(" difficult = ", 'green', attrs=['bold']), colored(difficult, 'white'))
    print(" ")
    logging.debug(f"run = {run}, difficult = {difficult}")
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
            error = raid.bottone()
            if error == 0:
                cprint(errore)
                return 0
            error = evoca.bottone()
            if error == 0:
                cprint(errore)
                return 0
            error = difficulty.bottone()
            if error == 0:
                cprint(errore)
                return 0
            error = accetta.bottone()
            if error == 0:
                cprint(errore)
                return 0
            # check if no shard is presence
            time.sleep(2)
            error = no_shard.ispresence()
            if error == 1:
                logging.debug("No shard available!")
                print("No shard!\n")
                pyautogui.press("esc")
                time.sleep(2)
                pyautogui.press("esc")
                time.sleep(2)
                pyautogui.press("esc")
                time.sleep(2)
                pyautogui.press("esc")
                return 0
            # else
            while True:
                # check if no shard is presence
                time.sleep(3)
                error = no_shard.ispresence()
                if error == 1:
                    logging.debug("No shard available!")
                    print("No shard!\n")
                    pyautogui.press("esc")
                    time.sleep(2)
                    return 0
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
                # -----------------------------------
                print("----------------------------------\n")
                if int(count) >= int(run):
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


async def fine():
    fine = classe.bit(r"image\fine.png", 0.7)
    while True:
        await asyncio.sleep(1)
        test = fine.SafeControl()
        if test == 1:
            return 1


async def test():
    prova = asyncio.create_task(fine())
    await prova
