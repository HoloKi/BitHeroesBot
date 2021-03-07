import pyautogui
import time
import json
import cv2 as cv
import logging


def gvg(run, tempo):
    conta = 1
    print("GVG")
    print(f"run = {run},tempo = {tempo}s")
    time.sleep(2)
    gvgbutton = pyautogui.locateCenterOnScreen(r"image\gvg.png", grayscale=False, confidence=0.5)
    if gvgbutton is not None:
        logging.debug(f"gvgbutton = {gvgbutton}")
        pyautogui.click(gvgbutton)
        time.sleep(5)
        while True:
            print(f"giro numero: {conta}")
            conta = int(conta) + 1
            play = pyautogui.locateCenterOnScreen(r"image\play.png", grayscale=False, confidence=0.5)
            if play is not None:
                logging.debug(f"play = {play}")
                pyautogui.click(play)
                time.sleep(5)
                battle = pyautogui.locateCenterOnScreen(r"image\battle1.png", grayscale=False, confidence=0.5)
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
                    else:
                        logging.debug(f"accept = {accept}")

                else:
                    print("Report this on github!")
                    logging.debug(f"battle = {battle}")
            else:
                print("Report this on github!")
                logging.debug(f"play = {play}")
    else:
        print("Gvg non disponibile o non riconosciuto. Nel caso spostati e ritenta")
        logging.debug(f"gvg not found! gvgbutton = {gvgbutton}")
