import pyautogui
import time
import cv2 as cv
import logging
from colorama import *
from termcolor import colored,cprint
init(autoreset=True); # Permette ad ogni print di ritornare al suo colore base


error = colored("Please report this bug/error on github",'red',attrs=['bold'])


def cimento(run, tempo):
    conta= 1;
    logging.debug(f"run = {run}, time = {tempo} seconds")
    cprint("\n-----CIMENTO-----",'cyan',attrs=['bold'])
    print(colored("run = ", 'green', attrs=['bold']), colored(run, 'white'),
          colored(" e durata = ", 'green', attrs=['bold']),
          colored(tempo, 'white'), colored("secondi\n", 'green'))
    if run <= 0:
        logging.debug("run < 1")
        pyautogui.alert(text="Run must be > 0", button="OK")
        exit(0)
    cimento = pyautogui.locateCenterOnScreen(r"image\cimento.png", grayscale=False, confidence=0.5)
    logging.debug(f"cimento button = {cimento}")
    if cimento is not None:
        pyautogui.click(cimento)
        while True:
            time.sleep(3)
            play = pyautogui.locateCenterOnScreen(r"image\play.png", grayscale=False, confidence=0.5)
            logging.debug(f"play = {play}")
            if play is not None:
                pyautogui.click(play)
                time.sleep(3)
                accept = pyautogui.locateCenterOnScreen(r"image\accept.png", grayscale=False, confidence=0.5)
                logging.debug(f'accept = {play}')
                if accept is not None:
                    print(colored("giro numero = ", 'green', attrs=['bold']), colored(conta, 'white'))
                    ciclo = int(ciclo) + 1
                    pyautogui.click(accept)
                    time.sleep(int(tempo))
                    close = pyautogui.locateCenterOnScreen(r"image\close.png", grayscale=False, confidence=0.5)
                    logging.debug(f'close = {close}')
                    if close is not None:
                        pyautogui.click(close)
                        time.sleep(3)
                        run = int(run) - 1
                        if int(run) == 0:
                            xbutton = pyautogui.locateCenterOnScreen(r"image\xbutton.png", grayscale=False, confidence=0.5)
                            if xbutton is not None:
                                pyautogui.click(xbutton)
                                break
                            else:
                                logging.debug(f'xbutton = {xbutton}')
                                print(error)
                                break
                    else:
                        logging.error("close is None")
                        print(error)
                        break
                else:
                    logging.error("accept is None")
                    print(error)
                    break
            else:
                logging.error("play is None")
                print(error)
                break
    else:
        logging.error(f'problem with cimento.png. return = {cimento}')
        cprint("Cimento non disponibile o non trovabile!",'red',attrs=['bold'])
        print(error)
        return 0