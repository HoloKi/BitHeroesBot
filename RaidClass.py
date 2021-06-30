import pyautogui
import time
import logging
import classe
from colorama import *
from termcolor import colored,cprint
import classe
init(autoreset=True) #Permette ad ogni print di ritornare al suo colore base

hero = "heroic"
hard = "hard"
norm = "normal"

error=colored("Please report this bug/error on github\n",'red',attrs=['bold'])
"""
Funzione Raid che utilizza la classe per semplificare il codice e il suo riutilizzo
@:param run = numero di run che fa il player (si presuppone che sia gia int)
@:param difficult = difficoltà del livello (si presuppone sia gia una stringa dal menu)
@:param duration = tempo in secondi per completare la run (si presuppone sia gia int)
@:return 1 se è andato tutto bene
@:return 0 se è andato storto
"""
def raid(run, difficult, duration):
    count=0;
    print(colored("\n-----RAID-----",'cyan',attrs=['bold']))
    print(colored("run = ",'green',attrs=['bold']),colored(run,'white'),colored(" difficult = ",'green',attrs=['bold']),colored(difficult,'white'),
          colored(" and duration = ",'green',attrs=['bold']), colored(duration,'white'),colored("seconds\n",'green',attrs=['bold']))
    logging.debug(f"run = {run}, difficoltà = {difficult}, durata = {duration}")
    time.sleep(3)
    # caso in cui le run sono minori di 0, ritorna 0
    if int(run) < 0:
        logging.debug("duration < 0")
        pyautogui.alert(text='the number of raid runs must be 1 or greater', button='OK')
        return 0
    else:
        # Caso in cui non voglio fare raid RUN=0, ritorna 0
        if int(run) == 0:
            logging.debug("run=0")
            return 0
        else:
            raid = classe.bit(r"image\prova.png",0.5)
            error = raid.bottone()
            evoca = classe.bit(r"image\startraid.png",0.5)
            evoca.bottone()
            eroico = classe.bit(r"image\eroic.png",0.5)
            eroico.bottone()
            accetta = classe.bit(r"image\accept.png",0.5)
            accetta.bottone()
            while(True):
                count += 1
                print(f"run number {count}\n")
                time.sleep(int(duration))
                if count==run:
                    si = classe.bit(r"image\yes.png",0.5)
                    si.bottone()
                    time.sleep(3)
                    pyautogui.press('esc')
                    break
                else:
                    pyautogui.press('esc')
                    time.sleep(5)

            print("test done")




