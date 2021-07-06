import pyautogui
import time
import logging
import classe
import sys
from colorama import *
from termcolor import colored,cprint
import classe
init(autoreset=True) #Permette ad ogni print di ritornare al suo colore base


errore=colored("Please report this bug/error on github or discord\n",'red',attrs=['bold'])
"""
Raid function that uses the class to simplify the code and its reuse
@: param run = number of runs that the player does (assumes it is already int)
@: param difficult = level difficulty (assumes it is already a string from the menu)
@: param duration = time in seconds to complete the run (assumes it is already int)
@: return 1 if everything went well
@: return 0 if it went wrong
"""
def raid(run, difficult, duration):
    hero = "heroic"
    hard = "hard"
    norm = "normal"
    difficulty = None #default
    count=0;
    # LOAD CLASS FIRST-----------------------------------------------------------------
    if difficult == hero:
        difficulty = classe.bit(r"image\raid\eroic.png",0.5)
    if difficult == hard:
        difficulty = classe.bit(r"image\raid\hard.png",0.5)
    if difficult == norm:
        difficulty = classe.bit(r"image\raid\normal.png",0.5)
    raid = classe.bit(r"image\raid\raid.png", 0.5)
    evoca = classe.bit(r"image\startraid.png",0.5)
    accetta = classe.bit(r"image\accept.png", 0.5)
    si = classe.bit(r"image\yes.png", 0.5)
    morte = classe.bit(r"image\raid\raiddie.png",0.7)
    chiudi = classe.bit(r"image\raid\close.png",0.5)
    #---------------------------------------------------------------------------------
    logging.debug(f"difficult = {difficulty}.")
    print(colored("\n-----RAID-----",'cyan',attrs=['bold']))
    print(colored("run = ",'green',attrs=['bold']),colored(run,'white'),
          colored(" difficult = ",'green',attrs=['bold']),colored(difficult,'white'),
          colored(" and duration = ",'green',attrs=['bold']), colored(duration,'white'),
          colored("seconds\n",'green',attrs=['bold']))
    logging.debug(f"run = {run}, difficoltà = {difficult}, durata = {duration}")
    time.sleep(3)
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
            accetta.bottone()
            if error == 0:
                cprint(errore)
                return 0
            while(True):
                count += 1
                print("----------------------------------")
                print(f"run number: {count}")
                timer(int(duration))
                print("----------------------------------\n")
                #controllo se è morto---------------
                error = morte.ispresence()
                if error == 1: #se è morto clicca
                    chiudi.bottone()
                    print("your team is dead!")
                    time.sleep(5)
                    pyautogui.press('esc')
                    break
                    return 0
                #-----------------------------------
                if int(count) >= int(run):
                    logging.debug("end")
                    error = si.bottone()
                    if error == 0:
                        cprint(errore)
                        print("Probably Insufficient time!")
                        break
                        return 0
                    else:
                        time.sleep(3)
                        pyautogui.press('esc')
                        break
                        return 1
                else:
                    pyautogui.press('esc')
                    time.sleep(3)



def timer(tempo):
    for i in range(int(tempo), 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write('remaining time: ' + str(i) + 's  ')
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r")
    sys.stdout.write("\033[K")

