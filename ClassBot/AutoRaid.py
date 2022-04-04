import pyautogui
import time
import logging
from colorama import *
from termcolor import colored, cprint
from ClassBot import Click_Class,classe
import asyncio
import json

init(autoreset=True)  # Permette ad ogni print di ritornare al suo colore base


"""
Raid function that uses the class to simplify the code and its reuse
@: param run = number of runs that the player does (assumes it is already int)
@: param difficult = level difficulty (assumes it is already a string from the menu)
@: param duration = time in seconds to complete the run (assumes it is already int)
@: return 1 if everything went well
@: return 0 if it went wrong
"""

def raid(run, difficult):
    #---------------------------------------------------------------
    f = open("data.json", "r")
    data = json.loads(f.read())

    raid_data = float(data['Function'][0]['raid'][0]['raid'])
    evoca_data = float(data['Function'][0]['raid'][0]['evoca'])
    accetta_data = float(data['Function'][0]['raid'][0]['accept'])
    chiudi_data = float(data['Function'][0]['raid'][0]['chiudi'])
    morte_data = float(data['Function'][0]['raid'][0]['morte'])
    rerun_data = float(data['Function'][0]['raid'][0]['rerun'])
    no_shard_data = float(data['Function'][0]['raid'][0]['no_shard'])
    difficult_data = float(data['Function'][0]['raid'][0]['difficult'])

    f.close()
    # --------------------------------------------------------------
    logging.debug("---------RAID----------")
    hero = "heroic"
    hard = "hard"
    norm = "normal"
    difficulty = None  # default
    count = 0
    # LOAD CLASS FIRST-----------------------------------------------------------------
    if difficult == hero:
        difficulty = Click_Class.bit(r"image\raid\heroic.png", difficult_data)
    else:
        if difficult == hard:
            difficulty = Click_Class.bit(r"image\raid\hard.png", difficult_data)
        else:
            if difficult == norm:
                difficulty = Click_Class.bit(r"image\raid\normal.png", difficult_data)

    raid = Click_Class.bit(r"image\raid\raid.png", raid_data)
    evoca = Click_Class.bit(r"image\startraid.png", evoca_data)
    accetta = Click_Class.bit(r"image\accept.png", accetta_data)
    chiudi = Click_Class.bit(r"image\raid\close.png", chiudi_data)
    morte = Click_Class.bit(r"image\raid\raiddie.png", morte_data)
    rerun = Click_Class.bit(r"image\rerun.png", rerun_data)
    no_shard = Click_Class.bit(r"image\noshard.png", no_shard_data)
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
            error = raid.search_and_click()
            if error == 0:
                return 0
            error = evoca.search_and_click()
            if error == 0:
                return 0
            error = difficulty.search_and_click()
            if error == 0:
                return 0
            error = accetta.search_and_click()
            if error == 0:
                return 0
            # check if no shard is presence after accept click
            time.sleep(2)
            error = no_shard.ispresence()
            # ------------- NO SHARDS
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
                # check if no shard is presence after rerun button
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
                    chiudi.search_and_click()
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
                    error = rerun.search_and_click()
                    if error == 0:
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
