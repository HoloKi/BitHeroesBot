import pyautogui
import time
import cv2 as cv
import logging
import sys
from colorama import *
from termcolor import colored,cprint
import classe

init(autoreset=True)  # Permette ad ogni print di ritornare al suo colore base

#repo = colored("C'è stato un problema con il bot. Segnalalo allo sviluppatore inviando il file ",'red') + "latest.log"
error = colored("Please report this bug/error on github or discord\n",'red',attrs=['bold'])

def pvp(run):
    #Caso in cui run <=0
    if run<=0:
        print(colored("Run <=0, skip PvP",'red'))
        logging.debug("Run<=0")
        return 0
    else:
        #load class-------------------------------------
        pvp = classe.bit(r"image\pvp.png",0.5)
        play = classe.bit(r"image\play.png",0.5)
        select = classe.bit(r"image\battle2.png",0.5)
        accetta = classe.bit(r"image\accept.png",0.5)
        defeat = classe.bit(r"image\defeat.png",0.5)
        chiudi = classe.bit(r"image\close.png",0.5)
        #-----------------------------------------------
        conta = 0
        errore = pvp.bottone()
        if errore == 0:
            cprint(error)
            return 0
        #timer(50)
        while(True):
            conta +=1
            errore = play.bottone()
            if errore == 0:
                cprint(error)
                break
                return 0
            errore = select.bottone()
            if errore == 0:
                cprint(error)
                break
                return 0
            errore = accetta.bottone()
            if errore == 0:
                cprint(error)
                break
                return 0
            time.sleep(50)
            # controllo se è morto---------------
            error = defeat.ispresence()
            if error == 1:  # se è morto clicca
                chiudi.bottone()
                print("Match Lost")
                time.sleep(2)
            # -----------------------------------

            if conta == int(run):
                pyautogui.press('esc')
                time.sleep(2)
                pyautogui.press('esc')
                print("test finito")
                break
                return 1
            else:
                pyautogui.press('esc')
                time.sleep(2)

def timer(tempo):
    for i in range(int(tempo), 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write('remaining time: ' + str(i) + 's  ')
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.flush()
    sys.stdout.write("\r")
    sys.stdout.write("--------------Done!--------------\n")
