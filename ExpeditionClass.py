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

def expedition(run,tempo):
    count = 0
    logging.debug(f"run = {run}, time = {tempo} seconds")
    cprint("\n-----EXPEDITION-----", 'cyan', attrs=['bold'])
    print(colored("run = ", 'green', attrs=['bold']), colored(run, 'white'),
          colored(" e durata = ",'green', attrs=['bold']),
          colored(tempo, 'white'), colored("secondi\n", 'green', attrs=['bold']))
    if run <= 0:
        logging.debug("run <= 0")
        pyautogui.alert(text="Run must be > 0", button="OK")
        exit(0)
    else:
        #load_class-------------------------
        expe = classe.bit(r"image\entra.png",0.5)
        accept = classe.bit(r"image\accept.png",0.5)
        xbutt = classe.bit(r"image\xbutton.png",0.5)
        yes = classe.bit(r"image\yes.png",0.5)
        #----------------------------------
        while(True):
            count += 1
            error = expe.bottone()
            if error == 0:
                cprint(errore)
                return 0
            error = accept.bottone()
            if error == 0:
                cprint(errore)
                return 0
            print("----------------------------------")
            print(f"Match n: {count}")
            time.sleep(int(tempo))
            print("----------------------------------\n")
            error = yes.bottone()
            if error == 0:
                cprint(errore)
                return 0
            if count == int(run):
                time.sleep(2)
                error = xbutt.bottone()
                if error == 0:
                    cprint(errore)
                    return 0
                pyautogui.press('esc')
                time.sleep(2)
                pyautogui.press('esc')
                break
