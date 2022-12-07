import pyautogui
import time
import logging
from colorama import *
from termcolor import colored, cprint
from ClassBot import Click_Class, classe
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
    elif difficult == hard:
        difficulty = Click_Class.bit(r"image\raid\hard.png", difficult_data)
    elif difficult == norm:
        difficulty = Click_Class.bit(r"image\raid\normal.png", difficult_data)

    raid = Click_Class.bit(r"image\raid\raid.png", raid_data)
    evoca = Click_Class.bit(r"image\startraid.png", evoca_data)
    accetta = Click_Class.bit(r"image\accept.png", accetta_data)
    chiudi = Click_Class.bit(r"image\raid\close.png", chiudi_data)
    morte = Click_Class.bit(r"image\raid\raiddie.png", morte_data)
    rerun = Click_Class.bit(r"image\rerun.png", rerun_data)
    no_shard = Click_Class.bit(r"image\noshard.png", no_shard_data)
    fine = Click_Class.bit(r"image\fine.png", 0.7)
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
            # TODO controllare se fallisce il click
            # TODO controllare se trova l'immagine
            res = asinc_run(x, 10)
            if res == -1:
                return 0
        # check if no shard is presence after accept click
        time.sleep(2)
        error = no_shard.is_present()
        # ------------- NO SHARDS -> turn back
        if error == True:
            # TODO rindondante quindi ciclo
            logging.debug("No shard available!")
            print("No shard!\n")
            for y in range(3):
                pyautogui.press("esc")
                time.sleep(2)
                return 0
        # else --------- WITH SHARDS
        while True:
            # check if no shard is presence after rerun button
            time.sleep(3)
            error = no_shard.is_present()
            if error == 1:
                logging.debug("No shard available!")
                print("No shard!\n")
                pyautogui.press("esc")
                time.sleep(2)
                return 0
            count += 1
            print("----------------------------------")
            print(f"run number: {count}")
            res = asinc_run(fine, 1000)  # THREAD che aspetta la schermata di fine partita
            if res == -1:
                return 0
            # controllo se è morto---------------
            error = morte.is_present()
            if error == True:  # se è morto clicca
                chiudi.search_and_click()
                print("your team is dead!")
                print("----------------------------------\n")
                time.sleep(5)
                pyautogui.press('esc')
                break
            # -----------------------------------
            print("----------------------------------\n")
            if int(count) >= int(run):  # If end run
                # controllare qui---------------
                # TODO semplificare sta parte
                for x in range(2):
                    time.sleep(4)
                    logging.debug("end")
                break
            else:
                res = asinc_run(rerun, 10)
                if res == -1:
                    return 0
                time.sleep(3)


#  Funzione che fa partirein modo asincrono  i bottoni iniziali
def asinc_run(file, timeout):
    # faccio runnare un thread per testare
    error = asyncio.run(test1(file, timeout))
    if error == -1:
        return -1


# trova il file, gira finche non trova se c'è l'immagine. se c'è clicca.
async def s_click(file):
    print(file.image)
    pos = 0
    while True:
        #TODO metterlo opzionale perchè consuma
        sys.stdout.write("\033[F")
        print("loading."+"."*(pos % 3)+"\r", end="\r")
        pos = pos + 1
        await asyncio.sleep(1)
        sys.stdout.write('\033[2K\033[1G')
        res = file.is_present()
        if res is True:
            time.sleep(1)
            while file.is_present() == True:  # Dovrei controllare se è andato a buon fine il click
                if file != fine:# Clicca se non è fine
                    #TODO da testare
                    file.search_and_click()
                    print("cliccato")
                return 1


# Dato un immagine crea una task dove deve riconoscere prova
async def test1(file, timeout):
    prova = asyncio.create_task(s_click(file))
    try:
        await asyncio.wait_for(prova, timeout=timeout)
    except Exception:
        sys.stdout.write('\033[2K\033[1G')
        cprint(colored("\nThe long operation timed out, probably image not found\n\n ",'red', attrs=['bold']))
        return -1



# -------------------------------------------------------------
