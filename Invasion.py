import pyautogui
import time
import cv2 as cv
import logging
from colorama import *
from termcolor import colored,cprint
init(autoreset=True) #Permette ad ogni print di ritornare al suo colore base


error = colored("Please report this bug/error on github",'red')


def invasione(run, tempo):
    print(colored("\n-----INVASIONE-----", 'cyan', attrs=['bold']))
    print(colored("run = ", 'green', attrs=['bold']), colored(run, 'white'), colored(" e durata = ", 'green', attrs=['bold']),
          colored(tempo, 'white'), colored("secondi\n", 'green', attrs=['bold']))
    conta = 1
    logging.debug(f"run = {run}, time = {tempo}")
    if run < 0:
        logging.debug("Run < 0")
        pyautogui.alert(text="Run must be > 0", button="OK")
        return 0
    else:
        if run == 0:
            print(colored("Skip Prove di Nyxn",'red', attrs=['bold']))
            return 0
        else:
            invasionebutton = pyautogui.locateCenterOnScreen(r"image\invasione.png", grayscale=False, confidence=0.5)
            logging.debug(f"bottone invasione = {invasionebutton}")
            if invasionebutton is not None:
                pyautogui.click(invasionebutton)
                while True:
                    time.sleep(3)
                    play = pyautogui.locateCenterOnScreen(r"image\play.png", grayscale=False, confidence=0.5)
                    logging.debug(f"play = {play}")
                    if play is not None:
                        pyautogui.click(play)
                        time.sleep(3)
                        accept = pyautogui.locateCenterOnScreen(r"image\accept.png", grayscale=False, confidence=0.5)
                        logging.debug(f"accept = {accept}")
                        if accept is not None:
                            pyautogui.click(accept)
                            print(colored("Giro numero = ", 'green', attrs=['bold']), colored(conta, 'white'))
                            time.sleep(int(tempo))
                            close = pyautogui.locateCenterOnScreen(r"image\close.png", grayscale=False, confidence=0.5)
                            logging.debug(f"close = {close}")
                            if close is not None:
                                pyautogui.click(close)
                                time.sleep(5)
                                run = int(run) - 1
                                conta = int(conta) + 1
                                if int(run) == 0:
                                    time.sleep(3)
                                    xbutton = pyautogui.locateCenterOnScreen(r"image\xbutton.png", grayscale=False,
                                                                             confidence=0.5)
                                    if xbutton is not None:
                                        pyautogui.click(xbutton)
                                        break
                                    else:
                                        logging.debug(f"xbutton = {xbutton}")
                                        print(error)
                                        break
                            else:
                                logging.debug("close is None")
                                print(error)
                                break
                        else:
                            logging.debug("accept is None")
                            print(error)
                            break
                    else:
                        logging.debug("play is None")
                        print(error)
                        break
                #End while -> tutto ok
                return 1
            else:
                logging.debug(f"problem with invasione.png. return = {invasionebutton} ")
                cprint("Invasione non disponibile o non lo trovo!", 'red', attrs=['bold'])
                print(error)
                return 0
