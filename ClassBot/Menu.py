import pyautogui
import time
import json
import logging
from ClassBot import AutoRaid, GvG, GauntletClass, ExpeditionClass, Invasion, NyxnTrial, PvPClass, Dungeon, DungeonAuto, checkers
from termcolor import colored, cprint


hero = "heroic"
hard = "hard"
norm = "normal"


def menu():
    print("\n\n")
    print(colored("Enter the number to select the desired option:\n", 'red', attrs=['bold']))
    print(colored("1) ", 'white'), colored("Raid", 'green', attrs=['bold']))
    print(colored("2) ", 'white'), colored("Pvp", 'green', attrs=['bold']))
    print(colored("3) ", 'white'), colored("Gauntlet", 'green', attrs=['bold']))
    print(colored("4) ", 'white'), colored("Change daily settings", 'red', attrs=['bold']))
    print(colored("5) ", 'white'), colored("Daily", 'green', attrs=['bold']))
    print(colored("6) ", 'white'), colored("Expedition", 'red', attrs=['bold']))
    print(colored("7) ", 'white'), colored("GvG", 'green', attrs=['bold']))
    print(colored("8) ", 'white'), colored("Nyxn Trial", 'red', attrs=['bold']))
    print(colored("9) ", 'white'), colored("Invasion", 'red', attrs=['bold']))
    print(colored("10)", 'white'), colored("Dungeon4", 'green', attrs=['bold']))
    print(colored("11)", 'white'), colored("Dungeon", 'green', attrs=['bold']))
    print(colored("check wiki to check how to set dungeon", 'red', attrs=['bold']))
    print(f"0)  To close the program\n")
    cprint("Select number: \n", 'cyan', attrs=['bold'])
    a = input()
    logging.debug(f'Menu input = {a}')
    if int(a) == 1:
        print(colored("Enter the number of runs: ", 'green', attrs=['bold']))
        b = input()
        print(colored("Enter the number:\n", 'green', attrs=['bold']), colored("1) normal\n"), colored("2) hard\n"),
              colored("3) heroic\n"), colored("According to the difficulty you want", 'green', attrs=['bold']))
        c = input()
        if int(c) == 1:
            retraid = AutoRaid.raid(b, norm)
            logging.debug(f"ritorno del raid = {retraid}")
            return 1
        else:
            if int(c) == 2:
                retraid = AutoRaid.raid(b, hard)
                logging.debug(f"ritorno del raid = {retraid}")
                return 1
            else:
                if int(c) == 3:
                    retraid = AutoRaid.raid(b, hero)
                    logging.debug(f"ritorno del raid = {retraid}")
                    return 1
                else:
                    print(colored("Something went wrong with typing the numbers", 'red', attrs=['bold']))
                    return 1
    else:
        if int(a) == 2:
            print(colored("ATTENTION: the bot will select the first one in the list by default!\n", 'red',
                          attrs=['bold']))
            cprint("How many pvp runs do you want to do?\n", 'green', attrs=['bold'])
            pvprun = input()
            PvPClass.pvp(int(pvprun))
            return 1
        else:
            if int(a) == 3:
                cprint("How many gauntlet runs do you want to do?", 'green', attrs=['bold'])
                cimentorun = input()
                GauntletClass.cimento(int(cimentorun))
                return 1
            else:
                if int(a) == 4:
                    setconfig()
                    return 1
                else:
                    if int(a) == 5:
                        cprint("ATTENTION: This command will initiate Raid, Pvp, Trial or Trials of Nynx!", 'red',
                               attrs=['bold'])
                        cprint("Make sure you have set the settings of the daily Command 4)", 'cyan', attrs=['bold'])
                        print(colored("Press", 'cyan', attrs=['bold']), colored("y", 'white'),
                              colored("if you are ready to start the daily, otherwise type", 'cyan', attrs=['bold']),
                              colored("n", 'white'))
                        sure = input()
                        if str(sure) == 'y':
                            daily()
                            return 1
                        else:
                            if str(sure) or int(sure):
                                return 1
                    else:
                        if int(a) == 6:
                            cprint("ATTENTION: This mode requires you to select expedition first!", 'red',
                                   attrs=['bold'])
                            cprint(
                                "You have to select which of the 3/4 shipments to make! The BOT will take care of the rest!",
                                'red', attrs=['bold'])
                            cprint("How many expedition runs do you want to do?", 'green', attrs=['bold'])
                            proverun = input()
                            ExpeditionClass.expedition(int(proverun))
                            return 1
                        else:

                            if int(a) == 7:
                                cprint("How many GvG runs do you want to do?", 'green', attrs=['bold'])
                                gvgrun = input()
                                GvG.gvg(int(gvgrun))
                                return 1
                            else:
                                if int(a) == 8:
                                    cprint("How many NyxnTrial runs do you want to do?", 'green', attrs=['bold'])
                                    exprun = input()
                                    NyxnTrial.prove(int(exprun))
                                    return 1
                                else:
                                    if int(a) == 9:
                                        cprint("How many invasion runs do you want to do?", 'green', attrs=['bold'])
                                        invrun = input()
                                        Invasion.invasione(int(invrun))
                                        return 1
                                    else:
                                        if int(a) == 10:
                                            cprint("How many dungeon4 runs do you want to do?", 'green', attrs=['bold'])
                                            dunrun = input()
                                            Dungeon.dungeon(int(dunrun))
                                            return 1
                                        else:
                                            if int(a) == 11:
                                                print(colored("Enter the number of runs: ", 'green', attrs=['bold']))
                                                b = input()
                                                print(colored("Enter the number:\n", 'green', attrs=['bold']),
                                                      colored("1) normal\n"), colored("2) hard\n"),
                                                      colored("3) heroic\n"),
                                                      colored("According to the difficulty you want", 'green',
                                                              attrs=['bold']))
                                                c = input()
                                                if int(c) == 1:
                                                    retraid = DungeonAuto.dungeonrepeat(b, norm)
                                                    logging.debug(f"ritorno del raid = {retraid}")
                                                    return 1
                                                else:
                                                    if int(c) == 2:
                                                        retraid = DungeonAuto.dungeonrepeat(b, hard)
                                                        logging.debug(f"ritorno del raid = {retraid}")
                                                        return 1
                                                    else:
                                                        if int(c) == 3:
                                                            retraid = DungeonAuto.dungeonrepeat(b, hero)
                                                            logging.debug(f"ritorno del raid = {retraid}")
                                                            return 1
                                                        else:
                                                            print(
                                                                colored("Something went wrong with typing the numbers",
                                                                        'red', attrs=['bold']))
                                                            return 1
                                            else:
                                                if int(a) == 0:
                                                    return 0
                                                else:
                                                    cprint("Non esiste un'opzione relativo a questo numero!", 'red',
                                                           attrs=['bold'])


"""
command to edit json file that store information about daily raid etc

"""


def setconfig():
    f = open("data.json", "r")
    data = json.loads(f.read())
    f.close()
    f = open("data.json", "w")
    cprint("Enter the number of raids you can do daily:", 'cyan', attrs=['bold'])
    a = input()
    cprint("For now the difficulty will be preset to heroic for error runtime", 'red', attrs=['bold'])
    # diff = input("Inserisci la difficoltà del raid\n")
    cprint("Enter the number of pvp runs you can do daily:", 'cyan', attrs=['bold'])
    b = input()
    cprint("Enter the number of Gauntlet / Trials runs you can do daily:", 'cyan', attrs=['bold'])
    c = input()
    data['name'] = checkers.USER
    data['raid'] = a
    data['difficulty'] = hero
    data['pvp'] = b
    data['gauntlet'] = c
    json.dump(data, f)
    f.close()


"""
Function to do daily task
"""


def daily():
    # loading daily from data.json-------
    f = open('data.json', "r")
    data = json.loads(f.read())
    raidshard = int(data['raid'])
    pvprun = int(data['pvp'])
    cimentorun = int(data['gauntlet'])
    f.close()
    # ------------------------------------

    AutoRaid.raid(int(raidshard), hero)
    time.sleep(5)
    PvPClass.pvp(int(pvprun))
    time.sleep(5)
    # prova a fare cimento. Se ritorna None, ritorna 0
    g = GauntletClass.cimento(int(cimentorun))
    if g == 0:
        NyxnTrial.prove(int(cimentorun))


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