import pyautogui
import time
import json
import cv2 as cv
import logging


def prove(run, tempo):
    print("\nPROVE\n")
    print(f"run = {run}, tempo per un completamento = {tempo}\n")
    conta = 1
    logging.debug(f"run = {run}, time = {tempo}")
    if run <= 0:
        logging.debug("Run < 1")
        pyautogui.alert(text="Run must be > 0", button="OK")
        exit(0)
    provebutton = pyautogui.locateCenterOnScreen(r"image\prove.png", grayscale=False, confidence=0.5)
    logging.debug(f"bottone prove = {provebutton}")
    if provebutton is not None:
        pyautogui.click(provebutton)
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
                    print(f"giro numero = {conta}")
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
                            xbutton = pyautogui.locateCenterOnScreen(r"image\xbutton.png", grayscale=False, confidence=0.5)
                            if xbutton is not None:
                                pyautogui.click(xbutton)
                                break
                            else:
                                logging.debug(f"xbutton = {xbutton}")
                                print("Please report this bug/error on github")
                                break
                    else:
                        logging.debug("close is None")
                        print("Please report this bug/error on github")
                        break
                else:
                    logging.debug("accept is None")
                    print("Please report this bug/error on github")
                    break
            else:
                logging.debug("play is None")
                print("Please report this bug/error on github")
                break
    else:
        logging.debug(f"problem with prove.png. return = {provebutton} ")
        print("Please report this bug/error on github")
        return 0
