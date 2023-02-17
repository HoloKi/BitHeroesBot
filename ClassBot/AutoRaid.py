import pyautogui
import time
import logging
from colorama import *
from termcolor import colored, cprint
from ClassBot import Click, classe
import asyncio
import json
import sys

init(autoreset=True)  # Permette ad ogni print di ritornare al suo colore base

"""
Raid function that uses the class to simplify the code and its reuse
@: param run = number of runs that the player does (assumes it is already int)
@: param difficult = level difficulty (assumes it is already a string from the menu)
@: param duration = time in seconds to complete the run (assumes it is already int)
@: return 1 if everything went well
@: return 0 if it went wrong
"""

loading = ["loading.", "loading..", "loading..."]


def raid(run, difficult):
    # ---------------------------------------------------------------
    f = open("data.json", "r")
    data = json.loads(f.read())
    #RIMOVIBILE SE FUNZIONA IL RESCALE
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
        difficulty = Click.immagini(r"image\raid\heroic.png", difficult_data)
    elif difficult == hard:
        difficulty = Click.immagini(r"image\raid\hard.png", difficult_data)
    elif difficult == norm:
        difficulty = Click.immagini(r"image\raid\normal.png", difficult_data)

    raid = Click.immagini(r"image\raid\raid.png", raid_data)
    evoca = Click.immagini(r"image\startraid.png", evoca_data)
    accetta = Click.immagini(r"image\accept.png", accetta_data)
    chiudi = Click.immagini(r"image\raid\close.png", chiudi_data)
    morte = Click.immagini(r"image\raid\raiddie.png", morte_data)
    rerun = Click.immagini(r"image\rerun.png", rerun_data)
    no_shard = Click.immagini(r"image\noshard.png", no_shard_data)
    fine = Click.immagini(r"image\fine.png", 0.7)
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
        arr = [raid, evoca, difficulty, accetta]
        for x in arr:
            # Fai partire thread che cliccano quando trovano l'immagine.
            res = Click.asinc_run(x, 10, True)
            if res == -1:
                return 0
        # check if no shard is presence after accept click
        time.sleep(2)
        error = Click.asinc_run(no_shard, 7, False)
        # ------------- NO SHARDS -> turn back
        print(f"errore del noshard {error}")
        if error is None:
            logging.debug("No shard available!")
            print("No shard!\n")
            for y in range(4):
                pyautogui.press("esc")
                time.sleep(2)
            return 0
        # else --------- WITH SHARDS
        while True:
            # check if no shard is presence after rerun button
            time.sleep(2)
            error = Click.asinc_run(no_shard, 13, False)
            if error is None:
                logging.debug("No shard available!")
                print("No shard!\n")
                pyautogui.press("esc")
                time.sleep(2)
                return 0
            count += 1
            print("----------------------------------")
            print(f"run number: {count}")
            res = Click.asinc_run(fine, 1000, False)  # THREAD che aspetta la schermata di fine partita
            if res == -1:
                return 0
            # controllo se è morto
            error = morte.is_present()
            if error:  # se è morto clicca #Error == True
                chiudi.search_and_click()
                print("your team is dead!")
                print("----------------------------------\n")
                time.sleep(5)
                pyautogui.press('esc')
                break
            # -----------------------------------
            print("----------------------------------\n")
            if int(count) >= int(run):  # Fine della Run
                time.sleep(3)
                for x in range(2):
                    time.sleep(5)
                    pyautogui.press('esc')
                    logging.debug("end")
                break
            else:
                print("PROVO A CLICCARE")
                asyncio.sleep(7)

                # Funziona ma da testare ancora meglio
                res = Click.asinc_run(rerun, 10, True)
                if res == -1:
                    return 0
