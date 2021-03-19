import pyautogui
import time
import cv2 as cv
import logging
from colorama import *
from termcolor import colored
init(autoreset=True)  # Permette ad ogni print di ritornare al suo colore base

repo = colored("C'è stato un problema con il bot. Segnalalo allo sviluppatore inviando il file ",'red') + "latest.log"
error = colored("Please report this bug/error on github",'red')

def pvp(run):
    #Caso in cui run <=0
    if run<=0:
        print(colored("Run <=0, skip PvP",'red'))
        logging.debug("Run<=0")
        return 0;
    else:
        conta = 1
        logging.debug(f"run = {run}")
        print(colored("\n-----PVP-----",'cyan',attrs=['bold']))
        print(colored("run = ",'green',attrs=['bold']),colored(run,'white'),colored("\n"))
        #Cerca il bottone del pvp
        pvp = pyautogui.locateCenterOnScreen(r"image\pvp.png", grayscale=False, confidence=0.5)
        logging.debug(f"pvp button = {pvp}")
        #Se c'è il bottone
        if pvp is not None:
            pyautogui.click(pvp)
            while True:
                time.sleep(2)
                play = pyautogui.locateCenterOnScreen(r"image\play.png", grayscale=False, confidence=0.5)
                logging.debug(f"play = {play}")
                if play is not None:
                    pyautogui.click(play)
                    time.sleep(2)
                    #Cerca la battaglia e clicca in quello piu alto cioè il primo
                    battle = pyautogui.locateCenterOnScreen(r"image\battle2.png", grayscale=False, confidence=0.5)
                    logging.debug(f"battle = {battle}")
                    if battle is not None:
                        pyautogui.click(battle)
                        time.sleep(2)
                        accept = pyautogui.locateCenterOnScreen(r"image\accept.png", grayscale=False, confidence=0.5)
                        logging.debug(f"accept = {accept}")
                        if accept is not None:
                            pyautogui.click(accept)
                            print(colored("giro numero = ",'green',attrs=['bold']),colored(conta,'white'))
                            time.sleep(40)
                            conta = int(conta) + 1
                            run = int(run) - 1
                            #Cerco il bottone close in caso di vittoria (verde)
                            close = pyautogui.locateCenterOnScreen(r"image\close.png", grayscale=False, confidence=0.9)
                            logging.debug(f"close = {close}")
                            if close is not None:
                                print(colored("Vittoria!",'blue',attrs=['bold']))
                                pyautogui.click(close)
                                time.sleep(2)
                                if int(run) == 0:
                                    xbutton = pyautogui.locateCenterOnScreen(r"image\xbutton.png", grayscale=False,
                                                                             confidence=0.5)
                                    logging.debug(f"xbutton = {xbutton}")
                                    if xbutton is not None:
                                        pyautogui.click(xbutton)
                                        break
                                    else:
                                        print(repo)
                                        logging.error("xbutton is None")
                                        print(error)
                                        break
                            else:
                                #Caso di sconfitta il bottone close (blu)
                                chiudi = pyautogui.locateCenterOnScreen(r"image\chiudi.png", grayscale=False,
                                                                        confidence=0.9)
                                logging.debug(f"Perso, chiudi= {chiudi}")
                                time.sleep(5)
                                #Se trova chiudi
                                if chiudi is not None:
                                    print(colored("Sconfitta!", 'red', attrs=['bold']))
                                    pyautogui.click(chiudi)
                                    time.sleep(5)
                                    if int(run) == 0:
                                        xbutton = pyautogui.locateCenterOnScreen(r"image\xbutton.png", grayscale=False,
                                                                             confidence=0.5)
                                        logging.debug(f"xbutton = {xbutton}")
                                        if xbutton is not None:
                                            pyautogui.click(xbutton)
                                            break
                                        else:
                                            print(repo)
                                            logging.error("xbutton is None")
                                            print(error)
                                            break
                                else:
                                    #Caso in cui non trova ne close ne chiudi ne close
                                    print(repo)
                                    logging.error("close  or chiudi is None")
                                    print(error)
                                    break
                        else:
                            print(repo)
                            logging.error("accept is None")
                            print(error)
                            break
                    else:
                        print(repo)
                        logging.error("battle is None")
                        print(error)
                        break
                else:
                    print(repo)
                    logging.error("play is None")
                    print(error)
                    break
            return 1
        else:
            print(colored("Non riesco a trovare il bottone pvp!",'red'))
            print(colored("Prova a spostarti o libera lo schermo!",'red'))
            logging.error(f"problem with pvp.png. pvp = {pvp}")
            print(error)
