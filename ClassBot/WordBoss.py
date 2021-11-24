import pyautogui
import time
import logging
from colorama import *
from termcolor import colored, cprint
from ClassBot import classe
import asyncio
import json

init(autoreset=True)  # Permette ad ogni print di ritornare al suo colore base

"""
WordBoss function that uses the class to simplify the code and its reuse
@: param run = number of runs that the player does (assumes it is already int)
@: param difficult = level difficulty (assumes it is already a string from the menu)
@: param duration = time in seconds to complete the run (assumes it is already int)
@: return 1 if everything went well
@: return 0 if it went wrong
"""


def raid(run, difficult):
    # ---------------------------------------------------------------
    f = open("data.json", "r")
    data = json.loads(f.read())

    wb_data = float(data['Function'][0]['wb'][0]['wb'])
    evoca1_data = float(data['Function'][0]['wb'][0]['evoca1'])
    evoca2_data = float(data['Function'][0]['wb'][0]['evoca2'])
    evoca3_data = float(data['Function'][0]['wb'][0]['evoca3'])
    inizio_data = float(data['Function'][0]['wb'][0]['inizio'])
    #morte_data = float(data['Function'][0]['wb'][0]['morte'])
    rerun_data = float(data['Function'][0]['wb'][0]['rerun'])
    #no_shard_data = float(data['Function'][0]['raid'][0]['no_shard'])
    end_data = float(data['Function'][0]['wb'][0]['end'])

    f.close()
    # --------------------------------------------------------------
    logging.debug("---------WORLD BOSS----------")
    count = 0
    # LOAD CLASS FIRST-----------------------------------------------------------------
    wb = classe.bit(r"image\wb\wb.png", wb_data)
    evoca1 = classe.bit(r"image\wb\wbevoca.png", evoca1_data)
    evoca2 = classe.bit(r"image\wb\wbevocagrande.png", evoca2_data)
    evoca3 = classe.bit(r"image\wb\wbevocapiccolo.png", evoca3_data)
    inizio = classe.bit(r"image\wb\startwb.png", inizio_data)
    #morte = classe.bit(r"image\wb\raiddie.png", morte_data)
    rerun = classe.bit(r"image\wb\rerun.png", rerun_data)
    cittadina = classe.bit(r"image\cittadina.png", end_data)
    #no_shard = classe.bit(r"image\wb\noshard.png", no_shard_data)
    # ---------------------------------------------------------------------------------
    print(colored("\n-----WORLD BOSS-----", 'cyan', attrs=['bold']))
    print(colored("run = ", 'green', attrs=['bold']), colored(run, 'white'))
    print(" ")
    logging.debug(f"run = {run}")
    # case in cui le run sono minori di 0, return 0
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
            # boss
            error = wb.bottone()
            if error ==1:
                return 0
            #evoca 1
            error = evoca1.bottone()
            if error ==1:
                return 0
            #evoca 2
            error = evoca2.bottone()
            if error == 1:
                return 0
            #evoca 3 -> evoca in modo da avere le impostazioni predefinite usate per ultimo
            error = evoca3.bottone()
            if error == 1:
                return 0
            while(True):
                count = count + 1
                # inizio -> restart from here
                error = inizio.bottone()
                if error == 1:
                    return 0
                # la tua squdra non è al completo, clicca si o enter (meglio enter, un immagine in meno)
                time.sleep(2)
                pyautogui.press('enter')
                # raggruppare o esc FINE
                if count == int(run):
                    error = cittadina.bottone()
                    if error == 1:
                        return 0
                else:
                    rerun.bottone()






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
