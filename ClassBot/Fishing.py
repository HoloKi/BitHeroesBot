import pyautogui
import time
import logging
from colorama import *
from termcolor import colored, cprint
from ClassBot import Click, classe
import asyncio
import json
import sys

#https://bit-heroes.fandom.com/wiki/Fishing

init(autoreset=True)  # Permette ad ogni print di ritornare al suo colore base

icon= Click.immagini("fishing.png",0.7)

def finishing():
    #clicco l'icona
    icon = Click.asinc_run(icon, 10, True);
    if icon == -1:
        return 0

