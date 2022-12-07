import pyautogui
import time
import json
import logging

from ClassBot import AutoRaid, GvG, GauntletClass, ExpeditionClass, Invasion, NyxnTrial, PvPClass, Dungeon4, Dungeon, \
    DeveloperMode, DungeonTeam, WorldBoss
from termcolor import colored, cprint

hero = "heroic"
hard = "hard"
norm = "normal"



def menu():
    #print("\n\n")
    print(colored("Enter the number to select the desired option:\n", 'red', attrs=['bold']))
    print(colored("1) ", 'white'), colored("Raid", 'green', attrs=['bold']))
    print(colored("2) ", 'white'), colored("Pvp", 'green', attrs=['bold']))
    print(colored("3) ", 'white'), colored("Gauntlet", 'green', attrs=['bold']))
    print(colored("4) ", 'white'), colored("DeveloperMode", 'green', attrs=['bold']))
    print(colored("5) ", 'white'), colored("OneForAll", 'green', attrs=['bold']))
    print(colored("6) ", 'white'), colored("Expedition", 'green', attrs=['bold']))
    print(colored("7) ", 'white'), colored("GvG", 'red', attrs=['bold']))
    print(colored("8) ", 'white'), colored("Nyxn Trial", 'green', attrs=['bold']))
    print(colored("9) ", 'white'), colored("Invasion", 'green', attrs=['bold']))
    print(colored("10)", 'white'), colored("Dungeon4", 'green', attrs=['bold']))
    print(colored("11)", 'white'), colored("Dungeon", 'green', attrs=['bold']))
    print(colored("12)", 'red'), colored("DungeonTeam", 'red', attrs=['bold']))
    print(colored("13)", 'white'), colored("World Boss", 'red', attrs=['bold']))
    print(colored("check wiki to check how to set dungeon", 'red', attrs=['bold']))
    print(f"0)  To close the program\n")
    cprint("Select number: \n", 'cyan', attrs=['bold'])
    a = input()
    # logging.debug(f'Menu input = {a}')
    try:
        if int(a) == 1:
            print(colored("\nEnter the number of runs: ", 'green', attrs=['bold']))
            b = input()
            print(colored("Enter the number:\n", 'green', attrs=['bold']), colored("1) normal\n"), colored("2) hard\n"),
                  colored("3) heroic\n"), colored("According to the difficulty you want", 'green', attrs=['bold']))
            c = input()
            if int(c) == 1:
                retraid = AutoRaid.raid(b, norm)
                # logging.debug(f"ritorno del raid = {retraid}")
                return 1
            elif int(c) == 2:
                retraid = AutoRaid.raid(b, hard)
                # logging.debug(f"ritorno del raid = {retraid}")
                return 1
            elif int(c) == 3:
                retraid = AutoRaid.raid(b, hero)
                # logging.debug(f"ritorno del raid = {retraid}")
                return 1
        elif int(a) == 2:
            print(colored("ATTENTION: the bot will select the first one in the list by default!\n", 'red',
                          attrs=['bold']))
            cprint("How many pvp runs do you want to do?\n", 'green', attrs=['bold'])
            pvprun = input()
            PvPClass.pvp(int(pvprun))
            return 1
        elif int(a) == 3:
            cprint("How many gauntlet runs do you want to do?", 'green', attrs=['bold'])
            cimentorun = input()
            GauntletClass.cimento(int(cimentorun))
            return 1
        elif int(a) == 4:
            while True:
                cycle = devmenu()
                if cycle == 0:
                    return 1
        elif int(a) == 5:
            cprint("ATTENTION: This command will consume all your\n"
                   " resources by doing everything", 'red',
                   attrs=['bold'])
            print(colored("Press", 'cyan', attrs=['bold']), colored("1", 'white'),
                  colored("if you want rerun Dungeon\n"
                          " otherwise for Dungeon4 type", 'cyan', attrs=['bold']),
                  colored("2", 'white'))
            sure = input()
            if int(sure) == 1:
                OneForAll(1)
                return 1
            else:
                if int(sure) == 2:
                    OneForAll(2)
                    return 1
                else:
                    print("something wrong")
        elif int(a) == 6:
            cprint("ATTENTION: This mode requires you to select expedition first!", 'red',
                   attrs=['bold'])
            cprint(
                "You have to select which of the 3/4 shipments to make! The BOT will take care of the rest!",
                'red', attrs=['bold'])
            cprint("How many expedition runs do you want to do?", 'green', attrs=['bold'])
            proverun = input()
            ExpeditionClass.expedition(int(proverun))
            return 1
        elif int(a) == 7:
            cprint("How many GvG runs do you want to do?", 'green', attrs=['bold'])
            gvgrun = input()
            GvG.gvg(int(gvgrun))
            return 1
        elif int(a) == 8:
            cprint("How many NyxnTrial runs do you want to do?", 'green', attrs=['bold'])
            exprun = input()
            NyxnTrial.prove(int(exprun))
            return 1
        elif int(a) == 9:
            cprint("How many invasion runs do you want to do?", 'green', attrs=['bold'])
            invrun = input()
            Invasion.invasione(int(invrun))
            return 1
        elif int(a) == 10:
            cprint("How many dungeon4 runs do you want to do?", 'green', attrs=['bold'])
            dunrun = input()
            Dungeon4.dungeon(int(dunrun))
            return 1
        # ------------
        # DUNGEON
        # ------------
        elif int(a) == 11:
            print(colored("Enter the number of runs: ", 'green', attrs=['bold']))
            b = input()
            print(colored("Enter the number:\n", 'green', attrs=['bold']),
                  colored("1) normal\n"), colored("2) hard\n"),
                  colored("3) heroic\n"),
                  colored("According to the difficulty you want", 'green',
                          attrs=['bold']))
            c = input()
            if int(c) == 1:
                retraid = Dungeon.dungeonrepeat(b, norm)
                return 1
            else:
                if int(c) == 2:
                    retraid = Dungeon.dungeonrepeat(b, hard)
                    return 1
                else:
                    if int(c) == 3:
                        retraid = Dungeon.dungeonrepeat(b, hero)
                        return 1
                    else:
                        print(
                            colored("Something went wrong with typing the numbers",
                                    'red', attrs=['bold']))
                        return 1
        elif int(a) == 12:
            print(colored("Enter the number of runs: ", 'green',
                          attrs=['bold']))
            b = input()
            DungeonTeam.dungeonteam(b)
        elif int(a) == 13:
            cprint(
                "ATTENTION: This mode requires you to select expedition first!",
                'red',
                attrs=['bold'])
            cprint(
                "You have to select which of the 3/4 shipments to make! The BOT will take care of the rest!",
                'red', attrs=['bold'])
            cprint("How many expedition runs do you want to do?", 'green',
                   attrs=['bold'])
            wbrun = input()
            WorldBoss.worldboss(wbrun)
            return 1
        else:
            if int(a) == 0:
                return 0
            else:
                cprint("Non esiste un'opzione relativo a questo numero!", 'red',
                       attrs=['bold'])
    except Exception as e:
        print(e)


'''
Function to do all functions 999 times
@param dungeon = select dungeon
@:return void 
'''


def OneForAll(dungeon):
    AutoRaid.raid(999, hero)
    time.sleep(5)
    PvPClass.pvp(999)
    time.sleep(5)
    # prova a fare cimento. Se ritorna None, ritorna 0
    g = GauntletClass.cimento(999)
    if g == 0:
        NyxnTrial.prove(999)
    time.sleep(5)
    Invasion.invasione(999)
    if int(dungeon) == 1:
        # Dungeon
        Dungeon.dungeonrepeat(999, hero)
    if int(dungeon) == 2:
        # Dungeon4
        Dungeon4.dungeon(999)


'''
DevMenu function menu about developer mode
'''


def devmenu():
    print("\n\n")
    print(colored("Enter the number to select the desired option:\n", 'red', attrs=['bold']))
    print(colored("1) ", 'white'), colored("Check&Click", 'green', attrs=['bold']))
    print(colored("2) ", 'white'), colored("Visibility", 'green', attrs=['bold']))
    print(colored("3) ", 'white'), colored("Debug", 'green', attrs=['bold']))
    print(colored("0) ", 'white'), colored("Close the program", 'green', attrs=['bold']))

    cprint("\nSelect number: \n", 'cyan', attrs=['bold'])
    a = input()
    logging.debug(f'Menu input = {a}')
    if int(a) == 1:
        print("Insert folder name, if is only image write image else raid or dungeon for the rispective folder\n")
        folder = input()
        print("Insert file name\n")
        name = input()
        print("Insert confidency, from 0.3 to 1 es : 0.5 (default)\n")
        confi = input()
        DeveloperMode.test(folder, name, confi)
    else:
        if int(a) == 2:
            print("Insert folder name, if is only image write image else raid or dungeon for the rispective folder\n")
            folder = input()
            print("Insert insert file name\n")
            name = input()
            print("Insert confidency, from 0.3 to 1 es : 0.5 (default)\n")
            confi = input()
            DeveloperMode.visibility(folder, name, confi)
        else:
            if int(a) == 3:
                DeveloperMode.debug()
            else:
                if int(a) == 0:
                    return 0
                else:
                    print("No funct with this number!")
                    return 0
