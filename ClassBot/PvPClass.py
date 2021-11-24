import pyautogui
import time
import logging
import asyncio
from colorama import *
from termcolor import colored, cprint
from ClassBot import classe
import json

init(autoreset=True)  # Permette ad ogni print di ritornare al suo colore base


def pvp(run):
    # -----------------------------------------------------
    f = open("data.json", "r")
    data = json.loads(f.read())

    pvp_data = float(data['Function'][0]['pvp'][0]['pvp'])
    play_data = float(data['Function'][0]['pvp'][0]['play'])
    select_data = float(data['Function'][0]['pvp'][0]['select'])
    accetta_data = float(data['Function'][0]['pvp'][0]['accept'])
    defeat_data = float(data['Function'][0]['pvp'][0]['defeat'])
    cittadina_data = float(data['Function'][0]['pvp'][0]['cittadina'])
    no_shard_data = float(data['Function'][0]['pvp'][0]['no_shard'])
    x = int(data['Function'][0]['class'][0]['x'])
    y = int(data['Function'][0]['class'][0]['y'])

    f.close()

    # -----------------------------------------------------

    logging.debug("---------PVP----------")
    problema = colored("Please report this bug/error on github or discord\n", 'red', attrs=['bold'])
    # Case run <=0
    if run <= 0:
        print(colored("Run <=0, skip PvP", 'red'))
        logging.debug("Run<=0")
        return 0
    else:
        print(colored("\n-----PVP-----", 'cyan', attrs=['bold']))
        print(colored("run = ", 'green', attrs=['bold']), colored(run, 'white'), colored("\n"))
        # load class-------------------------------------
        pvp = classe.bit(r"image\pvp.png", pvp_data)
        play = classe.bit(r"image\play.png", play_data)
        select = classe.bit(r"image\battle2.png", select_data)
        accetta = classe.bit(r"image\accept.png", accetta_data)
        defeat = classe.bit(r"image\sconfitta.png", defeat_data)
        cittadina = classe.bit(r"image\cittadina.png", cittadina_data)
        no_shard = classe.bit(r"image\noshard.png", no_shard_data)
        # -----------------------------------------------
        conta = 0
        error = pvp.bottone()
        if error == 0:
            cprint(problema)
            return 0
        while True:
            perso = False
            conta = int(conta) + 1
            error = play.bottone()
            if error == 0:
                cprint(problema)
                break
            # check if no shard is presence
            error = no_shard.SafeControl()
            if error == 1:
                logging.debug("No shard available!")
                pyautogui.press("esc")
                time.sleep(2)
                pyautogui.press("esc")
                return 0
            error = select.buttonmodif(x, y) #under test
            if error == 0:
                cprint(problema)
                break
            error = accetta.bottone()
            if error == 0:
                cprint(problema)
                break
            ''' 
            error = auto.ispresence()
            if error == 0:
                pyautogui.press('space')
            '''
            print("----------------------------------")
            print(f"Match n: {conta}")
            asyncio.run(test())
            # check if he die---------------
            error = defeat.ispresence()
            if error == 1:  # if he die click
                perso = True
                print("Match Lost")
            if error == 0:
                print("Winner!")
            # -----------------------------------
            print("----------------------------------\n")
            time.sleep(2)
            if perso == True:
                cittadina.bottone()
                time.sleep(2)
            if conta == int(run):
                if not perso:
                    # (perso == False)
                    pyautogui.press('esc')
                    time.sleep(2)
                pyautogui.press('esc')
                return 1
            else:
                if perso:
                    # (perso == True)
                    cittadina.bottone()
                    time.sleep(2)
                else:
                    pyautogui.press('esc')
                    time.sleep(2)
        return 0


async def fine():
    fine = classe.bit(r"image\pvpvick.png", 0.5)
    morte = classe.bit(r"image\raid\raiddie.png", 0.5)
    while True:
        await asyncio.sleep(1)
        test = morte.SafeControl()
        if test == 1:
            return 2
        test = fine.SafeControl()
        if test == 1:
            return 1


async def test():
    prova = asyncio.create_task(fine())
    await prova
