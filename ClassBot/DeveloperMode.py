import os.path
from ClassBot import *
import json
import logging

logging.basicConfig(filename="DeveloperLog.log", filemode="w", format='%(asctime)s - %(funcName)s :   %(message)s',
                        level=logging.DEBUG)

def Populate():
    # check if there isnt a data.json
    file = os.path.isfile("data.json")
    logging.debug(f"data.json = {file}")
    if file is True: # To edit cause i need this to debug
        f = open("data.json", "w")
        data = {'Function':[{
            'raid':[{
                'raid':'0.5',
                'evoca':'0.5',
                'accept':'0.5',
                'chiudi': '0.5',
                'morte': '0.5',
                'rerun':'0.5',
                'no_shard': '0.5'
            }],
            'pvp':[{
                'pvp': '0.5',
                'play': '0.5',
                'accetta': '0.5',
                'defeat': '0.5',
                'cittadina': '0.5',
                'no_shard': '0.5'
            }],
            'gauntlet':[{
                'gaunt': '0.5',
                'accept': '0.5',
                'play': '0.4',
                'no_shard': '0.5'
            }],
            'nynx_trial':[{
                'trial': '0.5',
                'accept': '0.5',
                'play': '0.4',
                'no_shard': '0.5'
            }],
            'gvg':[{
                'gvg':'0.5',
                'play' :'0.5',
                'select':'0.5',
                'accept':'0.5',
                'no_shard':'0.5'
            }],
            'expedition':[{
                'enter':'0.5',
                'accept':'0.5',
                'cittadina':'0.5'
            }],
            'invasion':[{
                'invasion': '0.5',
                'accept': '0.5',
                'play': '0.4',
                'no_shard': '0.5'
            }]
        }
        ]}

        json.dump(data,f, indent=4)
        f.close

'''
Test function
find image and click it
@:param name = String with file name es: "play.png"
@:param confidence = Float or Integer number from 0.3 to 1
@:return if image bot find image return cords or None
'''
def test(name, confidence):
    raidcord = pyautogui.locateCenterOnScreen(name, grayscale=False, confidence=confidence)
    print(raidcord)
    logging.debug(f"{name} with confidence {confidence} result {raidcord}")
    time.sleep(1)
    pyautogui.click(raidcord)
    return raidcord

'''
Test function
find image, no click
@:param name = String with file name es: "play.png"
@:param confidence = Float or Integer number from 0.3 to 1
@:return if image bot find image return cords or None
'''
def visibility(name, confidence):
    raidcord = pyautogui.locateCenterOnScreen(name, grayscale=False, confidence=confidence)
    print(raidcord)
    logging.debug(f"{name} with confidence {confidence} result {raidcord}")
    if raidcord is None:
        print("Image not found. Please change confidence or change the image with that of your game")


def debug():
    print(colored("Debug Mode on. Cerco tutte le immagini", 'red'))
    raid = pyautogui.locateCenterOnScreen(r"image\prova.png", grayscale=False, confidence=0.5)
    if raid is not None:
        print(colored("Raid funzionante!", 'blue', attrs=['bold']))
    else:
        print(f"Raid = {raid}")
    pvp = pyautogui.locateCenterOnScreen(r"image\pvp.png", grayscale=False, confidence=0.5)
    if pvp is not None:
        print(colored("PvP funzionante!", 'blue', attrs=['bold']))
    else:
        print(f"PvP = {pvp}")
    gvg = pyautogui.locateCenterOnScreen(r"image\gvg.png", grayscale=False, confidence=0.5)
    if gvg is not None:
        print(colored("GvG Presente!", 'blue', attrs=['bold']))
    else:
        print(f"GvG = {gvg}")
    cimento = pyautogui.locateCenterOnScreen(r"image\cimento.png", grayscale=False, confidence=0.5)
    if cimento is not None:
        print(colored("Cimento presente!", 'blue', attrs=['bold']))
    else:
        print(f"Cimento = {cimento}")
    prove = pyautogui.locateCenterOnScreen(r"image\prove.png", grayscale=False, confidence=0.5)
    if prove is not None:
        print(colored("Prove presente!", 'blue', attrs=['bold']))
    else:
        print(f"Prove di Nyxn = {prove}")
    invasione = pyautogui.locateCenterOnScreen(r"image\invasione.png", grayscale=False, confidence=0.5)
    if invasione is not None:
        print(colored("Invasione presente!", 'blue', attrs=['bold']))
    else:
        print(f"Invasione = {invasione}")
    print(colored("\nNel caso ci fossero dei None, assicurati che siano disponibili, in tal caso spostati", 'red',
                  attrs=['bold']))
    time.sleep(5)
    return 1



