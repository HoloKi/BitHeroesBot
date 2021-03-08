import pyautogui
import time
import cv2 as cv
import logging
from colorama import *
from termcolor import colored,cprint
init(autoreset=True) #Permette ad ogni print di ritornare al suo colore base


error=colored("Please report this bug/error on github\n", 'red', attrs=['bold'])

def spedizione(run, tempo):
    conta = 1
    logging.debug(f"run = {run}, time = {tempo} seconds")
    cprint("\n-----SPEDIZIONE-----", 'blue', attrs=['bold'])
    print(colored("run = ", 'green', attrs=['bold']), colored(run, 'white'), colored(" e durata = ",
        'green', attrs=['bold']),colored(tempo, 'white'), colored("secondi\n", 'green', attrs=['bold']))
    if run <= 0:
        logging.debug("run < 1")
        pyautogui.alert(text="Run must be > 0", button="OK")
        exit(0)
    else:
        while True:
            enter = pyautogui.locateCenterOnScreen(r"image\entra.png", grayscale=False, confidence=0.5)
            logging.debug(f"enter = {enter}")
            #Se trova il bottone enter
            if enter is not None:
                time.sleep(3)
                pyautogui.click(enter)
                time.sleep(2)
                accetta = pyautogui.locateCenterOnScreen(r"image\accept.png", grayscale=False, confidence=0.9)
                logging.debug(f"accept = {accetta}")
                #Se trova accetta
                if accetta is not None:
                    time.sleep(3)
                    pyautogui.click(accetta)
                    print(colored("Giro numero = ", 'green', attrs=['bold']), colored(conta,'white'))
                    #tempo per eseguire tutto il percorso
                    time.sleep(int(tempo))
                    run = int(run) - 1
                    conta = int(conta) + 1
                    yes = pyautogui.locateCenterOnScreen(r"image\yes.png", grayscale=False, confidence=0.5)
                    logging.debug(f"yes = {yes}")
                    #pulsante yes
                    if yes is not None:
                        time.sleep(3)
                        pyautogui.click(yes)
                        #termine della run
                        if run == 0:
                            time.sleep(5)
                            xbutton = pyautogui.locateCenterOnScreen(r"image\xbutton1.png", grayscale=False, confidence = 0.9)
                            logging.debug(f"xbutton1 = {xbutton}")
                            pyautogui.click(xbutton)
                            time.sleep(2)
                            #cicla 2 volte
                            for i in range(2):
                                xbutton = pyautogui.locateCenterOnScreen(r"image\xbutton.png", grayscale=False, confidence=0.5)
                                logging.debug(f"xbutton = {xbutton}")
                                time.sleep(3)
                                if xbutton is not None:
                                    pyautogui.click(xbutton)
                                    time.sleep(2)
                                else:
                                    logging.error("xbutton missing")
                                    break
                            break
                        else:
                            time.sleep(5)
                    else:
                        #Caso in cui non trovo yes, probabilmente morto
                        close = pyautogui.locateCenterOnScreen(r"image\chiudi.png", grayscale=False, confidence=0.5)
                        logging.debug(f"Morto! close = {close}")
                        if close is not None:
                            time.sleep(3)
                            pyautogui.click(close)
                        else:
                            logging.debug("close or yes not found")
                            cprint("Possibile che il tempo sia inferiore al dovuto!",'red',attrs=['bold'])
                            print(error)
                            break
                else:
                    logging.debug("accetta not found")
                    print(error)
                    break
            else:
                logging.debug("enter not found!")
                print(error)
                break
        return 1
