import os.path

from termcolor import colored

from ClassBot import *
import json
import logging
import pyautogui
import traceback
import os
import time


def Populate():
    # check if there isnt a data.json
    file = os.path.isfile("data.json")
    logging.debug(f"data.json = {file}")
    if file is False:  # To edit cause i need this to debug
        f = open("data.json", "x")
        data = {'Function': [{
            'raid': [{
                'raid': '0.5',
                'evoca': '0.5',
                'accept': '0.5',
                'chiudi': '0.5',
                'morte': '0.7',
                'rerun': '0.5',
                'no_shard': '0.5',
                'difficult': '0.7'
            }],
            'pvp': [{
                'pvp': '0.5',
                'play': '0.4',
                'accept': '0.5',
                'select': '0.5',
                'defeat': '0.6',
                'cittadina': '0.5',
                'no_shard': '0.5'
            }],
            'gauntlet': [{
                'gaunt': '0.5',
                'accept': '0.5',
                'play': '0.4',
                'no_shard': '0.5'
            }],
            'nynx_trial': [{
                'trial': '0.5',
                'accept': '0.5',
                'play': '0.4',
                'no_shard': '0.5'
            }],
            'gvg': [{
                'gvg': '0.5',
                'play': '0.5',
                'select': '0.5',
                'accept': '0.5',
                'no_shard': '0.5'
            }],
            'expedition': [{
                'enter': '0.5',
                'accept': '0.6',
                'cittadina': '0.5'
            }],
            'invasion': [{
                'invasion': '0.5',
                'accept': '0.5',
                'play': '0.4',
                'no_shard': '0.5'
            }],
            'dungeon': [{
                'quest': '0.5',
                'dungeon': '0.5',
                'accept': '0.5',
                'chiudi': '0.5',
                'morte': '0.7',
                'rerun': '0.5',
                'no_shard': '0.5',
                'difficult': '0.7'
            }],
            'dungeonfour': [{
                'quest': '0.5',
                'dungeon': '0.5',
                'enter': '0.5',
                'accept': '0.5',
                'chiudi': '0.5',
                'morte': '0.7',
                'rerun': '0.5',
                'no_shard': '0.5'
            }]
        }
        ]}
        json.dump(data, f, indent=4)
        f.close()

    else:
        return 0


'''
Test function
find image and click it
@:param folder
@:param name = String with file name es: "play.png"
@:param confidence = Float or Integer number from 0.3 to 1
@:return if image bot find image return cords or None
ES: raid,hard.png,0.5
'''


def test(folder, name, confidence):
    imageFolder()

    if str(folder) == "raid":
        os.chdir("raid")
    if str(folder) == "dungeon":
        os.chdir("dungeon")
    logging.debug(f"current directory {os.getcwd()}")
    try:
        raidcord = pyautogui.locateCenterOnScreen(name, grayscale=False, confidence=confidence)
        print(raidcord)
        logging.debug(f"{name} with confidence {confidence} result {raidcord}")
        if raidcord is not None:
            time.sleep(1)
            pyautogui.click(raidcord)
            return 0
    except Exception as e:
        logging.error(traceback.format_exc())
        logging.debug(f"error with test name {name} and confidence {confidence}")
        print("name or confidence error!")


'''
Test function
find image, no click
@:param name = String with file name es: "play.png"
@:param confidence = Float or Integer number from 0.3 to 1
@:return if image bot find image return cords or None
'''


def visibility(folder, name, confidence):
    imageFolder()

    if str(folder) == "raid":
        os.chdir("raid")
    if str(folder) == "dungeon":
        os.chdir("dungeon")
    logging.debug(f"current directory {os.getcwd()}")
    try:
        raidcord = pyautogui.locateCenterOnScreen(name, grayscale=False, confidence=confidence)
        print(raidcord)
        logging.debug(f"{name} with confidence {confidence} result {raidcord}")
        if raidcord is None:
            print("Image not found. Please change confidence or change the image with that of your game")
    except Exception as e:
        logging.error(traceback.format_exc())
        logging.debug(f"error with test name {name} and confidence {confidence}")
        print("name or confidence error!")


def debug():
    print(colored("Debug Mode on. Cerco tutte le immagini", 'red'))
    raid = pyautogui.locateCenterOnScreen(r"image\raid\raid.png", grayscale=False, confidence=0.5)
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


'''
ImageFolder()
Function to return into folder Image -> visibility and test 
@:param nothing
'''


def imageFolder():
    # actually folder
    now = os.path.basename(os.getcwd())
    if now != "image":
        try:
            # if its on BitHeroes main folder go to C:...\image
            os.chdir("image")
            return 0
        except:
            # if its on image\raid or image\dungeon, urn back into image folder
            now = os.path.basename(os.getcwd())
            while str(now) != "image":
                os.chdir("..")
                now = os.path.basename(os.getcwd())
    else:
        return 0
