import pyautogui
import time
import logging
import asyncio
from colorama import *
from termcolor import colored, cprint
from ClassBot import classe
import json

init(autoreset=True)  # Permette ad ogni print di ritornare al suo colore base
errore = colored("Please report this bug/error on github", 'red', attrs=['bold'])


def cimento(run):
    #--------------
    f = open("data.json", "r")
    data = json.loads(f.read())

    gaunt_data = float(data['Function'][0]['gauntlet'][0]['gaunt'])
    play_data = float(data['Function'][0]['gauntlet'][0]['play'])
    accept_data = float(data['Function'][0]['gauntlet'][0]['accept'])
    no_shard_data = float(data['Function'][0]['gauntlet'][0]['no_shard'])
    f.close()
    #--------------

    logging.debug("---------GAUNTLET----------")
    conta = 0
    logging.debug(f"run = {run}")
    cprint("\n-----GAUNTLET-----", 'cyan', attrs=['bold'])
    print(colored("run = ", 'green', attrs=['bold']), colored(run, 'white'))
    print(" ")
    if run <= 0:
        logging.debug("run <= 0")
        pyautogui.alert(text="Run must be > 0", button="OK")
        return 0
    else:
        # load-----------------------------
        gaunt = classe.bit(r"image\cimento.png", gaunt_data)
        play = classe.bit(r"image\play.png", play_data)
        accept = classe.bit(r"image\accept.png", accept_data)
        no_shard = classe.bit(r"image\noshard.png", no_shard_data)
        # ---------------------------------
        error = gaunt.bottone()
        if error == 0:
            cprint(errore)
            return 0
        while True:
            conta += 1
            error = play.bottone()
            if error == 0:
                cprint(errore)
                return 0
            # check if no shard is presence
            error = no_shard.SafeControl()
            if error == 1:
                logging.debug("No shard available!")
                pyautogui.press("esc")
                time.sleep(2)
                pyautogui.press("esc")
                return 0
            # case have shard
            error = accept.bottone()
            if error == 0:
                cprint(errore)
                return 0
            '''
            error = auto.ispresence()
            if error == 0:
                pyautogui.press('space')
            '''
            print("----------------------------------")
            print(f"run number: {conta}")
            asyncio.run(test())
            print("----------------------------------\n")
            time.sleep(2)
            if conta == int(run):
                pyautogui.press('esc')
                time.sleep(3)
                pyautogui.press('esc')
                break
            else:
                pyautogui.press('esc')
                time.sleep(2)


async def fine():
    vittoria = classe.bit(r"image\cittadina.png", 0.5)
    no_shard = classe.bit(r"image\noshard.png", 0.5)
    while True:
        await asyncio.sleep(1)
        test = vittoria.SafeControl()
        if test == 1:
            return 1 # return 2 in caso ci sia sconfitta


async def test():
    prova = asyncio.create_task(fine())
    await prova
