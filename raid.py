import pyautogui
import time
import cv2 as cv
import logging
import classe
from colorama import *
from termcolor import colored,cprint
init(autoreset=True) #Permette ad ogni print di ritornare al suo colore base

hero = "heroic"
hard = "hard"
norm = "normal"

error=colored("Please report this bug/error on github\n",'red',attrs=['bold'])

# run = numero di shard
# difficult = difficoltà
# duration = quanto dura in secondi una run
# ritorna 1 se tutto va bene, in caso 0. il break va solo nel ciclo while
def raid(run, difficult, duration):
    conta = 1
    print(colored("\n-----RAID-----",'cyan',attrs=['bold']))
    print(colored("run = ",'green',attrs=['bold']),colored(run,'white'),colored(" difficolta = ",'green',attrs=['bold']),colored(difficult,'white'),
          colored(" e durata = ",'green',attrs=['bold']), colored(duration,'white'),colored("secondi\n",'green',attrs=['bold']))
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
            raidcord = pyautogui.locateCenterOnScreen(r"image\prova.png", grayscale=False, confidence=0.5)
            logging.debug(f"raid button = {raidcord}. If None, to fix it, change position in the screen.")
            if raidcord is not None:
                pyautogui.click(raidcord)
                time.sleep(2)
                #Controllo che abbia shard per fare il raid NONE= ha shard, se lo trova invece non ha shard
                shardcheck = pyautogui.locateCenterOnScreen(r"image\noshard.png", grayscale=False, confidence=0.9)
                logging.debug(f"shardcheck = {shardcheck}. if None its ok!")
                if shardcheck is None:
                    evoca = pyautogui.locateCenterOnScreen(r"image\startraid.png", grayscale=False, confidence=0.5)
                    logging.debug(f"evoca = {evoca}.")
                    if evoca is not None:
                        pyautogui.click(evoca)
                        time.sleep(3)
                        if difficult == hero:
                            difficulty = pyautogui.locateCenterOnScreen(r"image\eroic.png", grayscale=False,
                                                                        confidence=0.5)
                        if difficult == hard:
                            difficulty = pyautogui.locateCenterOnScreen(r"image\hard.png", grayscale=False,
                                                                        confidence=0.5)
                        if difficult == norm:
                            difficulty = pyautogui.locateCenterOnScreen(r"image\normal.png", grayscale=False,
                                                                        confidence=0.5)
                        logging.debug(f"difficult = {difficulty}.")
                        if difficulty is not None:
                            pyautogui.click(difficulty)
                            time.sleep(2)
                            accept = pyautogui.locateCenterOnScreen(r"image\accept.png", grayscale=False,
                                                                    confidence=0.5)
                            logging.debug(f"accept = {accept}")
                            if accept is not None:
                                pyautogui.click(accept)
                                # tempo dedicato al completamento del raid in auto
                                while True:
                                    print(colored(f"giro numero = ",'green', attrs=['bold']),colored(conta,'white'))
                                    time.sleep(int(duration))
                                    if int(run) == 1:
                                        yes = pyautogui.locateCenterOnScreen(r"image\yes.png", grayscale=False,
                                                                             confidence=0.5)
                                        logging.debug(f"yes = {yes}")
                                        time.sleep(3)
                                        if yes is not None:
                                            pyautogui.click(yes)
                                            time.sleep(5)
                                            xbutton = pyautogui.locateCenterOnScreen(r"image\xbutton.png",
                                                                                     grayscale=False,
                                                                                     confidence=0.5)
                                            logging.debug(f"xbutton = {xbutton}")
                                            time.sleep(5)
                                            pyautogui.click(xbutton)
                                            break
                                        else:
                                            #Se è morto e yes è None cioè non trova il bottone
                                            close = pyautogui.locateCenterOnScreen(r"image\chiudi.png",grayscale=False,
                                                                                   confidence=0.5)
                                            logging.debug(f"close= {close}")
                                            if close is not None:
                                                time.sleep(3)
                                                pyautogui.click(close)
                                                return 0
                                            else:
                                                cprint("Tempo impostato non sufficiente!",'red',attrs=['bold'])
                                                return 0

                                    else:
                                        conta = int(conta) + 1
                                        run = int(run) - 1
                                        rerun = pyautogui.locateCenterOnScreen(r"image\rerun.png", grayscale=False,
                                                                               confidence=0.5)
                                        logging.debug(f"rerun = {rerun}")
                                        time.sleep(3)
                                        if rerun is None:
                                            #Controlla che il giocatore sia morto
                                            close = pyautogui.locateCenterOnScreen(r"image\chiudi.png",grayscale=False,
                                                                                   confidence=0.5)
                                            if close is None:
                                                #Se non è morto allora esce dalla funzione
                                                print(colored("Probabilmente il tempo non era impostato bene!",'red'))
                                                return 0;
                                            else:
                                                #se è morto clicca su close;
                                                pyautogui.click(close);
                                                return 0
                                        else:
                                            #Se può fare la rerun
                                            pyautogui.click(rerun)
                                #Fine della funzione
                                return 1

                            else:
                                print("Tasto accept non trovato!")
                                logging.error("Accept error, please send this to github issue")
                                print(error)
                                return 0
                        else:
                            print("Tasto della difficolta non trovato!")
                            logging.error("Difficult error, please send this to github issue")
                            print(error)
                            return 0
                    else:
                        print("Tasto evoca non trovato!")
                        logging.debug("Evoca is none, please send this to github issue")
                        print(error)
                        return 0
                else:
                    print(colored("Shard non disponibili!\n",'red'))
                    logging.debug("No shard")
                    time.sleep(5)
                    xbutton = pyautogui.locateCenterOnScreen(r"image\xbutton.png", grayscale=False, confidence=0.5)
                    logging.debug(f"xbutton = {xbutton}")
                    pyautogui.click(xbutton)
            else:
                print("Tasto Raid non trovato!\n")
                logging.debug("Raid is None,please report this error on github")
                print("Prova a spostarti un pochino e riprova il comando!\n")
                return 0


def raidclass(run, tipo,tempo):
    p1 = classe.bit(r"image\prova.png",0.5)
    p = p1.bottone()
    time.sleep(2)
    logging.debug(f"p1.bott={p}")
    if p1 != 0:
        p2 = classe.bit(r"image\startraid.png",0.5)
        p2.bottone()
        time.sleep(2)
        if p2!=0:
            p3 = classe.bit(r"image\eroic.png",0.5)
            p3.bottone()
            time.sleep(2)
            if p3!=0:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0;
