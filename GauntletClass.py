import pyautogui
import time
import cv2 as cv
import logging
import sys
from colorama import *
from termcolor import colored,cprint
import classe

init(autoreset=True)  # Permette ad ogni print di ritornare al suo colore base
errore = colored("Please report this bug/error on github",'red',attrs=['bold'])

def cimento(run, tempo):
    conta = 0
    logging.debug(f"run = {run}, time = {tempo} seconds")
    cprint("\n-----CIMENTO-----", 'cyan', attrs=['bold'])
    print(colored("run = ", 'green', attrs=['bold']), colored(run, 'white'),
          colored(" e durata = ", 'green', attrs=['bold']),
          colored(tempo, 'white'), colored("secondi\n", 'green'))
    if run <= 0:
        logging.debug("run <= 0")
        pyautogui.alert(text="Run must be > 0", button="OK")
        return 0
    else:
        #load-----------------------------
        gaunt = classe.bit(r"image\cimento.png",0.5)
        play = classe.bit(r"image\play.png",0.4)
        accept = classe.bit(r"image\accept.png",0.5)
        #---------------------------------
        error = gaunt.bottone()
        if error == 0:
            cprint(errore)
            return 0
        while(True):
            conta += 1
            error = play.bottone()
            if error == 0:
                cprint(errore)
                return 0
            error = accept.bottone()
            if error == 0:
                cprint(errore)
                return 0
            print("----------------------------------")
            print(f"run number: {conta}")
            timer(int(tempo))
            print("----------------------------------\n")
            if conta==int(run):
                pyautogui.press('esc')
                time.sleep(3)
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