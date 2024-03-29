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
Dungeon function that uses the class to simplify the code and its reuse
@: param run = number of runs that the player does (assumes it is already int)
@: param difficult = level difficulty (assumes it is already a string from the menu)
@: param duration = time in seconds to complete the run (assumes it is already int)
@: return 1 if everything went well
@: return 0 if it went wrong
"""


def dungeonrepeat(run, difficult):
    # ---------------------------------------------------------------
    f = open("data.json", "r")
    data = json.loads(f.read())

    quest_data = float(data['Function'][0]['dungeon'][0]['quest'])
    dungeon_data = float(data['Function'][0]['dungeon'][0]['dungeon'])
    accetta_data = float(data['Function'][0]['dungeon'][0]['accept'])
    chiudi_data = float(data['Function'][0]['dungeon'][0]['chiudi'])
    morte_data = float(data['Function'][0]['dungeon'][0]['morte'])
    rerun_data = float(data['Function'][0]['dungeon'][0]['rerun'])
    difficult_data = float(data['Function'][0]['dungeon'][0]['difficult'])

    no_shard_data = float(data['Function'][0]['dungeon'][0]['no_shard'])
    f.close()
    # --------------------------------------------------------------
    logging.debug("---------DUNGEON----------")
    hero = "heroic"
    hard = "hard"
    norm = "normal"
    difficulty = None  # default
    count = 0
    # LOAD CLASS FIRST-----------------------------------------------------------------
    if difficult == hero:
        difficulty = classe.bit(r"image\raid\heroic.png", difficult_data)
    else:
        if difficult == hard:
            difficulty = classe.bit(r"image\raid\hard.png", difficult_data)
        else:
            if difficult == norm:
                difficulty = classe.bit(r"image\raid\normal.png", difficult_data)
    quest = classe.bit(r"image\quest.png",quest_data)
    dungeon = classe.bit(r"image\dungeon\dungeon.png", dungeon_data)
    accetta = classe.bit(r"image\accept.png", accetta_data)
    chiudi = classe.bit(r"image\raid\close.png", chiudi_data)
    morte = classe.bit(r"image\raid\raiddie.png", morte_data)
    rerun = classe.bit(r"image\rerun.png", rerun_data)
    noteam = classe.bit(r"image\noteam.png", 0.5)
    # ---------------------------------------------------------------------------------
    logging.debug(f"difficult = {difficulty.getImage()}.")
    print(colored("\n-----DUNGEON-----", 'cyan', attrs=['bold']))
    print(colored("run = ", 'green', attrs=['bold']), colored(run, 'white'),
          colored(" difficult = ", 'green', attrs=['bold']), colored(difficult, 'white'))
    print(" ")
    logging.debug(f"run = {run}, difficoltà = {difficult}")
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
            error = quest.bottone()
            if error == 0:
                cprint(errore)
                return 0
            error = dungeon.bottone()
            if error == 0:
                cprint("Probably something gone wrong with screen")
                cprint("Please check the wiki or discord server!")
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
            error = noteam.ispresence()
            if error == 1:
                pyautogui.press('enter')

            while True:
                ''' cause error #see discord support
                error = auto.ispresence()
                if error == 0:
                    logging.debug("auto is not green")
                    pyautogui.press('space')
                '''
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
