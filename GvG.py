import pyautogui
import time
import cv2 as cv
import logging
from colorama import *
from termcolor import colored,cprint
init(autoreset=True) # Permette ad ogni print di ritornare al suo colore base


def gvg(run, tempo):
    conta = 1
    print(colored("\n-----GVG-----",'cyan',attrs=['bold']))
    print(colored("run = ", 'green',attrs=['bold']), colored(run, 'white'),colored(" e durata = ", 'green',attrs=['bold']),
          colored(tempo, 'white'), colored("secondi\n", 'green',attrs=['bold']))
    time.sleep(2)
    gvgbutton = pyautogui.locateCenterOnScreen(r"image\gvg.png", grayscale=False, confidence=0.5)
    if gvgbutton is not None:
        logging.debug(f"gvgbutton = {gvgbutton}")
        pyautogui.click(gvgbutton)
        time.sleep(5)
        while True:
            print(colored("giro numero = ",'green',attrs=['bold']),colored(conta,'white'))
            conta = int(conta) + 1
            play = pyautogui.locateCenterOnScreen(r"image\play.png", grayscale=False, confidence=0.5)
            if play is not None:
                logging.debug(f"play = {play}")
                pyautogui.click(play)
                time.sleep(5)
                battle = pyautogui.locateCenterOnScreen(r"image\battle1.png", grayscale=False, confidence=0.2)
                if battle is not None:
                    logging.debug(f"battle = {battle}")
                    pyautogui.click(battle)
                    time.sleep(5)
                    accept = pyautogui.locateCenterOnScreen(r"image\accept.png", grayscale=False, confidence=0.5)
                    if accept is not None:
                        logging.debug(f"accept = {accept}")
                        pyautogui.click(accept)
                        time.sleep(int(tempo))
                        chiudi = pyautogui.locateCenterOnScreen(r"image\close.png", grayscale=False, confidence=0.5)
                        if chiudi is not None:
                            logging.debug(f"close = {chiudi}")
                            pyautogui.click(chiudi)
                            time.sleep(5)
                            if run == 1:
                                xbutton = pyautogui.locateCenterOnScreen(r"image\xbutton.png", grayscale=False, confidence=0.5)
                                pyautogui.click(xbutton)
                                break
                            else:
                                run = int(run) - 1
                        else:
                            logging.debug(f"close = {chiudi}")
                            break;
                    else:
                        logging.debug(f"accept = {accept}")
                        break;

                else:
                    print("Report this on github!")
                    logging.debug(f"battle = {battle}")
                    break;
            else:
                print("Report this on github!")
                logging.debug(f"play = {play}")
                break;
    else:
        cprint("Gvg non disponibile o non riconosciuto. Nel caso spostati e ritenta",'red',attrs=['bold'])
        logging.debug(f"gvg not found! gvgbutton = {gvgbutton}")
