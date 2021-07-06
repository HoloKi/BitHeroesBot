import pyautogui
import time
import cv2 as cv
import logging
import sys
from colorama import *
from termcolor import colored,cprint
import classe

init(autoreset=True)  # Permette ad ogni print di ritornare al suo colore base


def pvp(run):
    error = colored("Please report this bug/error on github or discord\n", 'red', attrs=['bold'])
    #Case run <=0
    if run<=0:
        print(colored("Run <=0, skip PvP",'red'))
        logging.debug("Run<=0")
        return 0
    else:
        print(colored("\n-----PVP-----", 'cyan', attrs=['bold']))
        print(colored("run = ", 'green', attrs=['bold']), colored(run, 'white'), colored("\n"))
        #load class-------------------------------------
        pvp = classe.bit(r"image\pvp.png",0.5)
        play = classe.bit(r"image\play.png",0.4)
        select = classe.bit(r"image\battle2.png",0.5)
        accetta = classe.bit(r"image\accept.png",0.5)
        defeat = classe.bit(r"image\defeat.png",0.7)
        chiudi = classe.bit(r"image\chiudi.png",0.5)
        #-----------------------------------------------
        conta = 0
        errore = pvp.bottone()
        if errore == 0:
            cprint(error)
            return 0
        #timer(50)
        while(True):
            conta = int(conta) + 1
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
            #time.sleep(50)
            print("----------------------------------")
            print(f"Match n: {conta}")
            timer(40)
            # check if he die---------------
            error = defeat.ispresence()
            if error == 1:  # if he die click
                chiudi.bottone()
                print("Match Lost")
                time.sleep(2)
            if error == 0:
                print("Winner!")
            # -----------------------------------
            print("----------------------------------\n")

            if conta == int(run):
                pyautogui.press('esc')
                time.sleep(2)
                pyautogui.press('esc')

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
    sys.stdout.write("\r")
    sys.stdout.write("\033[K")
