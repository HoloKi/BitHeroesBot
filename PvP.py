import pyautogui
import time
import cv2 as cv
import logging


def pvp(run):
    conta = 1
    logging.debug(f"run = {run}")
    print("\n-----PVP-----\n")
    print(f"run = {run}\n")
    if run <= 0:
        pyautogui.alert(text="Run must be > 0", button="OK")
        logging.debug("run < 1")
        exit()
    pvp = pyautogui.locateCenterOnScreen(r"image\pvp.png", grayscale=False, confidence=0.5)
    logging.debug(f"pvp button = {pvp}")
    if pvp is not None:
        pyautogui.click(pvp)
        while True:
            time.sleep(2)
            play = pyautogui.locateCenterOnScreen(r"image\play.png", grayscale=False, confidence=0.5)
            logging.debug(f"play = {play}")
            if play is not None:
                pyautogui.click(play)
                time.sleep(2)
                battle = pyautogui.locateCenterOnScreen(r"image\battle1.png", grayscale=False, confidence=0.5)
                logging.debug(f"battle = {battle}")
                if battle is not None:
                    pyautogui.click(battle)
                    time.sleep(2)
                    accept = pyautogui.locateCenterOnScreen(r"image\accept.png", grayscale=False, confidence=0.5)
                    logging.debug(f"battle = {battle}")
                    if accept is not None:
                        pyautogui.click(accept)
                        print(f"giro numero = {conta}")
                        time.sleep(100)
                        conta = int(conta) + 1
                        close = pyautogui.locateCenterOnScreen(r"image\close.png", grayscale=False, confidence=0.5)
                        logging.debug(f"close = {close}")
                        if close is not None:
                            pyautogui.click(close)
                            time.sleep(2)
                            run = int(run) - 1
                            if int(run) == 0:
                                xbutton = pyautogui.locateCenterOnScreen(r"image\xbutton.png", grayscale=False, confidence=0.5)
                                logging.debug(f"xbutton = {xbutton}")
                                if xbutton is not None:
                                    pyautogui.click(xbutton)
                                    break
                                else:
                                    logging.error("xbutton is None")
                                    print("Please report this bug/error on github")
                                    break
                        else:
                            logging.error("close is None")
                            print("Please report this bug/error on github")
                            break
                    else:
                        logging.error("accept is None")
                        print("Please report this bug/error on github")
                        break
                else:
                    logging.error("battle is None")
                    print("Please report this bug/error on github")
                    break
            else:
                logging.error("play is None")
                print("Please report this bug/error on github")
                break
        return 1
    else:
        logging.error(f"problem with pvp.png. pvp = {pvp}")
        print("Please report this bug/error on github")
