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
import ctypes
import asyncio

load_dotenv()

init(autoreset=True)  # Permette ad ogni print di ritornare al suo colore base
errore = colored("Please report this bug/error on github or discord\n", 'red', attrs=['bold'])

# default perchè le immagini vengono dal mio pc
game_width, game_height = 800, 480
monitor_width, monitor_height = 1366, 768

user32 = ctypes.windll.user32
# specs monitor utente
monitor_x = user32.GetSystemMetrics(0)  # width
monitor_y = user32.GetSystemMetrics(1)  # height

# Calculate the scaling factor for the image
scaling_factor_width = monitor_width / game_width
scaling_factor_height = monitor_height / game_height


class immagini:
    def __init__(self, image, confi):
        self.image = image
        self.confi = confi
        self.debug = os.getenv('DEBUG')
        self.count = 0

    # Function to find image and click it
    # buttons return (x,y) as coordinates or None if image not found
    def search_and_click(self):

        # Faccio lo screenshot dell'intero monitor pc
        screen = pyautogui.screenshot()
        # lo apro con opencv in bianco e nero
        img = cv.cvtColor(numpy.array(screen), cv.COLOR_BGR2GRAY)
        # Faccio il canny + edge del gioco
        canny_screenshot = cv.Canny(img, 100, 200)
        img_da_confrontare = cv.imread(self.image, 0)
        w, h = img_da_confrontare.shape[::-1]
        logging.debug(f"dim immagine prima {w, h}")

        # print("mio", monitor_width, monitor_height, "utente", monitor_x, monitor_y)
        # sottraggo proporzione immagine gioco mio con quello dell'utente per ottenere la differenza di proporzione
        user_x = monitor_x / game_width
        user_y = monitor_y / game_height

        diff_x = 1 + (user_x - scaling_factor_width)
        diff_y = 1 + (user_y - scaling_factor_height)
        print(diff_x, diff_y)
        logging.debug(f"differenza= {diff_x, diff_y}")
        try:
            resized_image = cv.resize(img_da_confrontare, (0, 0), fx=diff_x, fy=diff_y)
            if self.debug == '1' and diff_x != 0.0 and diff_y != 0.0:
                w, h = resized_image.shape[::-1]
                logging.debug(f"dim immagine dopo {w, h}")
                test = pathlib.Path(__file__).parent.resolve()
                cv.imwrite("{self.count}" + "resized.png", resized_image)
                self.count = int(self.count) + 1

            # Funzione per confrontare le due immagini
            canny_img_confronto = cv.Canny(resized_image, 100, 200)
            res = cv.matchTemplate(canny_screenshot, canny_img_confronto, cv.TM_CCOEFF)
        except Exception as e:
            print(e)

        # logging.debug(f"risultato match= {res}")
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
        res = no_shard.is_present()
        if res == True:
            print("No shards!")
        else:
            print("Ok!")

    # is_present  without debug control so no spam on logging
    def is_present(self):
        if self.debug == 1:
            print(self.image)
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


#  Funzione che fa partirein modo asincrono  i bottoni iniziali
def asinc_run(file, timeout, flag):
    # faccio runnare un thread per testare
    error = asyncio.run(test1(file, timeout, flag))
    if error == -1:
        return -1


# trova il file, gira finche non trova se c'è l'immagine. se c'è clicca.
async def s_click(file):
    print(file.image)
    pos = 0
    while True:
        # TODO metterlo opzionale perchè consuma
        sys.stdout.write("\033[F")
        print("loading." + "." * (pos % 3) + "\r", end="\r")
        pos = pos + 1
        await asyncio.sleep(1)
        sys.stdout.write('\033[2K\033[1G')
        res = file.is_present()
        if res is True:
            file.search_and_click()
            print("clicked")
            return 1


async def s_search(file):
    pos = 0
    while True:
        # TODO metterlo opzionale perchè consuma
        sys.stdout.write("\033[F")
        print("searching." + "." * (pos % 3) + "\r", end="\r")
        pos = pos + 1
        await asyncio.sleep(1)
        sys.stdout.write('\033[2K\033[1G')
        res = file.is_present()
        if res is True:  # Quando trova l'immagine
            print("immagine presente")
            time.sleep(3)
            return 1


# Dato un immagine crea una task dove deve riconoscere prova
async def test1(file, timeout, flag):
    if not flag:  # flag == False
        prova = asyncio.create_task(s_search(file))
    else:
        prova = asyncio.create_task(s_click(file))
    try:
        print(prova)
        await asyncio.wait_for(prova, timeout=timeout)
    except Exception:
        sys.stdout.write('\033[2K\033[1G')
        cprint(colored("\nThe long operation timed out, probably image not found\n\n ", 'red', attrs=['bold']))
        return -1


#  Funzione che fa partirein modo asincrono  i bottoni iniziali

def asinc_run(file, timeout, flag):
    # faccio runnare un thread per testare
    error = asyncio.run(test1(file, timeout, flag))
    if error == -1:
        return -1


# trova il file, gira finche non trova se c'è l'immagine. se c'è clicca.
async def s_click(file):
    print(file.image)
    pos = 0
    while True:
        # TODO metterlo opzionale perchè consuma
        sys.stdout.write("\033[F")
        print("loading." + "." * (pos % 3) + "\r", end="\r")
        pos = pos + 1
        await asyncio.sleep(1)
        sys.stdout.write('\033[2K\033[1G')
        res = file.is_present()
        if res is True:
            file.search_and_click()
            print("clicked")
            return 1


async def s_search(file):
    pos = 0
    while True:
        # TODO metterlo opzionale perchè consuma
        sys.stdout.write("\033[F")
        print("searching." + "." * (pos % 3) + "\r", end="\r")
        pos = pos + 1
        await asyncio.sleep(1)
        sys.stdout.write('\033[2K\033[1G')
        res = file.is_present()
        if res is True:  # Quando trova l'immagine
            print("immagine presente")
            time.sleep(3)
            return 1


# Dato un immagine crea una task dove deve riconoscere prova
async def test1(file, timeout, flag):
    if not flag:  # flag == False
        prova = asyncio.create_task(s_search(file))
    else:
        prova = asyncio.create_task(s_click(file))
    try:
        print(prova)
        await asyncio.wait_for(prova, timeout=timeout)
    except Exception:
        sys.stdout.write('\033[2K\033[1G')
        cprint(colored("\nThe long operation timed out, probably image not found\n\n ", 'red', attrs=['bold']))
        return -1
