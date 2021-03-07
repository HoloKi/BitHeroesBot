import pyautogui
import time
import json
import cv2 as cv
import logging

hero = "heroic"
hard = "hard"
norm = "normal"

# run = numero di shard
# difficult = difficoltà
# duration = quanto dura in secondi una run
# ritorna 1 se tutto va bene, in caso 0. il break va solo nel ciclo while
def raid(run, difficult, duration):
    conta = 1
    print("\nRAID\n")
    print(f"run = {run}, difficolta = {difficult} e durata = {duration} secondi\n")
    logging.debug(f"run = {run}, difficoltà = {difficult}, durata = {duration}")
    time.sleep(3)
    # caso in cui le run sono minori di 1, ritorna 0
    if int(run) < 1:
        logging.debug("duration < 1")
        pyautogui.alert(text='the number of raid runs must be 1 or greater', button='OK')
        return 0
    else:
        raidcord = pyautogui.locateCenterOnScreen(r"image\prova.png", grayscale=False, confidence=0.6)
        logging.debug(f"raid button = {raidcord}. If None, to fix it, change position in the screen.")
        if raidcord is not None:
            pyautogui.click(raidcord)
            time.sleep(2)
            shardcheck = pyautogui.locateCenterOnScreen(r"image\noshard.png", grayscale=False, confidence=0.9)
            logging.debug(f"shardcheck = {shardcheck}. if None its ok!")
            if shardcheck is None:
                evoca = pyautogui.locateCenterOnScreen(r"image\startraid.png", grayscale=False, confidence=0.5)
                logging.debug(f"evoca = {evoca}.")
                if evoca is not None:
                    pyautogui.click(evoca)
                    time.sleep(3)
                    if difficult == hero:
                        difficulty = pyautogui.locateCenterOnScreen(r"image\eroic.png", grayscale=False, confidence=0.4)
                    if difficult == hard:
                        difficulty = pyautogui.locateCenterOnScreen(r"image\hard.png", grayscale=False, confidence=0.5)
                    if difficult == norm:
                        difficulty = pyautogui.locateCenterOnScreen(r"image\normal.png", grayscale=False, confidence=0.5)
                    # if difficult != norm and difficult != hard and difficult != hero:
                    #    print("error")
                    #    log("difficult error, probably not norm,hard or hero", "a")
                    #    exit()
                    logging.debug(f"difficult = {difficulty}.")
                    if difficulty is not None:
                        pyautogui.click(difficulty)
                        time.sleep(2)
                        accept = pyautogui.locateCenterOnScreen(r"image\accept.png", grayscale=False, confidence=0.5)
                        logging.debug(f"accept = {accept}")
                        if accept is not None:
                            pyautogui.click(accept)
                            # tempo dedicato al completamento del raid in auto
                            while True:
                                print(f"giro numero = {conta}")
                                time.sleep(int(duration))
                                if int(run) == 1:
                                    yes = pyautogui.locateCenterOnScreen(r"image\yes.png", grayscale=False, confidence=0.5)
                                    logging.debug(f"yes = {yes}")
                                    time.sleep(3)
                                    if yes is not None:
                                        pyautogui.click(yes)
                                        time.sleep(5)
                                        xbutton = pyautogui.locateCenterOnScreen(r"image\xbutton.png", grayscale=False,
                                                                                 confidence=0.5)
                                        logging.debug(f"xbutton = {xbutton}")
                                        time.sleep(5)
                                        pyautogui.click(xbutton)
                                        break
                                    else:
                                        print("Tempo impostato non sufficiente!")
                                        return 0

                                else:
                                    conta = int(conta) + 1
                                    run = int(run) - 1
                                    rerun = pyautogui.locateCenterOnScreen(r"image\rerun.png", grayscale=False, confidence=0.5)
                                    logging.debug(f"rerun = {rerun}")
                                    time.sleep(3)
                                    pyautogui.click(rerun)
                            return 1

                        else:
                            print("Tasto accept non trovato!\n")
                            logging.error("AcceptError, please send this to github issue")
                            print("Please report this bug/error on github\n")
                            return 0
                    else:
                        print("Tasto della difficolta non trovato!\n")
                        logging.error("Difficult error, please send this to github issue")
                        print("Please report this bug/error on github\n")
                        return 0
                else:
                    print("Tasto evoca non trovato!r\n")
                    logging.debug("Evoca is none, please send this to github issue")
                    print("Please report this bug/error on github\n")
                    return 0
            else:
                print("Shard non disponibili!\n")
                logging.debug("No shard")
                time.sleep(5)
                xbutton = pyautogui.locateCenterOnScreen("xbutton.png", grayscale=False, confidence=0.5)
                logging.debug(f"xbutton = {xbutton}")
                pyautogui.click(xbutton)
        else:
            print("Tasto Raid non trovato!\n")
            logging.debug("Raid is None,please report this error on github")
            print("Prova a spostarti un pochino e riprova il comando!\n")
            return 0
