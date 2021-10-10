import pyautogui
import time
import logging
from colorama import *
from termcolor import colored, cprint
from ClassBot import classe
import asyncio

init(autoreset=True)  # Permette ad ogni print di ritornare al suo colore base

errore = colored("Please report this bug/error on github or discord\n", 'red', attrs=['bold'])


def prove(run):
    # --------------
    f = open("data.json", "r")
    data = json.loads(f.read())

    trial_data = float(data['Function'][0]['nynx_trial'][0]['gaunt'])
    play_data = float(data['Function'][0]['nynx_trial'][0]['play'])
    accept_data = float(data['Function'][0]['nynx_trial'][0]['accept'])
    no_shard_data = float(data['Function'][0]['nynx_trial'][0]['no_shard'])
    f.close()
    # --------------
    logging.debug("---------NYXN-TRIAL----------")
    print(colored("\n-----NYXN-TRIAL-----", 'cyan', attrs=['bold']))
    print(colored("run = ", 'green', attrs=['bold']), colored(run, 'white'))
    conta = 0
    logging.debug(f"run = {run}")
    if run < 0:
        logging.debug("Run < 0")
        pyautogui.alert(text="Run must be > 0", button="OK")
        return 0
    else:
        if run == 0:
            print(colored("Skip Prove di Nyxn", 'red', attrs=['bold']))
            return 0
        else:
            # load_class---------------------------
            trial = classe.bit(r"image\prove.png", trial_data)
            play = classe.bit(r"image\play.png", play_data)
            accept = classe.bit(r"image\accept.png", accept_data)
            no_shard = classe.bit(r"image\noshard.png", no_shard_data)
            # -------------------------------------
            error = trial.bottone()
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
                pyautogui.press('esc')
                time.sleep(3)
                if conta == int(run):
                    pyautogui.press('esc')
                    break


async def fine():
    fine = classe.bit(r"image\cittadina.png", 0.7)
    #morte = classe.bit(r"image\raid\raiddie.png", 0.7)
    while True:
        await asyncio.sleep(1)
        test = fine.ispresence()
        if test == 1:
            return 1


async def test():
    prova = asyncio.create_task(fine())
    await prova
