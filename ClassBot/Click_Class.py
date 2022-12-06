import pyautogui
import time
import logging
from colorama import *
from termcolor import colored, cprint
import sys
import json
from dotenv import load_dotenv
import cv2 as cv
import os
import numpy
from PIL import Image
import pathlib

load_dotenv()

init(autoreset=True)  # Permette ad ogni print di ritornare al suo colore base
errore = colored("Please report this bug/error on github or discord\n", 'red', attrs=['bold'])


class bit:
    def __init__(self, image, confi):
        self.image = image
        self.confi = confi
        self.debug = os.getenv('DEBUG')
        self.count = 0

    # Function to find image and click it
    # button return (x,y) as coordinates or None if image not found
    #
    def search_and_click(self):
        print(os.getenv('DEBUG'))
        # Faccio lo screenshot dell'intero monitor pc
        screen = pyautogui.screenshot()
        # lo apro con opencv in bianco e nero
        img = cv.cvtColor(numpy.array(screen), cv.COLOR_BGR2GRAY)
        # Faccio il canny + edge del gioco
        canny_screenshot = cv.Canny(img, 100, 200)
        img_da_confrontare = cv.imread(self.image, 0)
        w, h = img_da_confrontare.shape[::-1]
        canny_img_confronto = cv.Canny(img_da_confrontare, 100, 200)

        # Funzione per confrontare le due immagini
        res = cv.matchTemplate(canny_screenshot, canny_img_confronto, cv.TM_CCOEFF)
        logging.debug(f"risultato match= {res}")
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        # Calcolo il centro dell'immagine
        x, y = self.center(top_left, bottom_right)
        logging.debug(f"posizione click  = {x, y}")
        logging.debug(f"debug  = {self.debug}")
        if self.debug == '1':
            print("disegno")
            # Draw Rectangle
            cv.rectangle(img, top_left, bottom_right, 255, 1)
            # cv.circle(screen, (x, y), radius=0, color=(255, 0, 0), thickness=10)
            print("salvo")
            im = Image.fromarray(img)
            test = pathlib.Path(__file__).parent.resolve()
            im.save(rf"{test}\Debug\{self.count}" + "raid.png")
            self.count = int(self.count) + 1

        button = pyautogui.click(x, y)
        logging.debug(f"{self.getImage()} = {button}")
        time.sleep(2)  # debug purpose

    def center(self, x1, y1):
        x2 = ((y1[0] - x1[0]) / 2) + x1[0]
        y2 = ((y1[1] - x1[1]) / 2) + x1[1]
        return int(x2), int(y2)

    # Comando per vedere se un immagine è presente
    def is_present_log(self):
        presente = pyautogui.locateCenterOnScreen(self.image, grayscale=False, confidence=float(self.confi))
        logging.debug(f"{self.image} presence = {presente}")
        if presente is not None:
            return True
        else:
            return False


    def no_shardControl(self):
        no_shard = self.__init__(r"image\noshard.png", 0.5)
        res = no_shard.ispresence()
        if res == 1:
            print("No shards!")
        else:
            print("Ok!")

    # is_present  without debug control so no spam on logging
    def is_present(self):
        presente = pyautogui.locateCenterOnScreen(self.image, grayscale=False, confidence=float(self.confi))
        if presente is not None:
            return True
        else:
            return False

    def timer(self):
        for i in range(10, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write('remaining time: ' + str(i) + 's  ')
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\r")
        sys.stdout.write("\033[K")

    def getImage(self):
        return self.image

    # Function to find image and click it
    # button return (x,y) as coordinates or None if image not found
    # using x,y to permit x editing (right)
    # modifier
    def buttonmodif(self, xmodifier, ymodifier):
        x, y = pyautogui.locateCenterOnScreen(self.image, grayscale=False, confidence=float(self.confi))
        logging.debug(f"{self.getImage()} = {(x, y)}")
        if (x, y) is not None:
            time.sleep(3)
            pyautogui.click(x + int(xmodifier), y + int(ymodifier))
            time.sleep(1)
            return 1
        else:
            cprint(f"Error, {self.image} not found!", "red", attrs=['bold'])
            cprint(errore)
            logging.error(f"{self.image} not found!")
            return 0
