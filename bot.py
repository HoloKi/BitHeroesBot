import pyautogui
import time
import json
import logging
import RaidClass
import GauntletClass
import ExpeditionClass
import PvPClass
import ProveN
from colorama import *
from termcolor import colored,cprint

init(autoreset=True);

VERSION = "5.1.3"

hero = "heroic"
hard = "hard"
norm = "normal"

def menu():
    print("\n\n")
    print(colored("Enter the number to select the desired option:\n",'red',attrs=['bold']))
    print(colored("1) ",'white'),colored("Raid",'green',attrs=['bold']))
    print(colored("2) ",'white'),colored("Pvp",'green',attrs=['bold']))
    print(colored("3) ",'white'),colored("Gauntlet",'green',attrs=['bold']))
    print(colored("4) ",'white'),colored("Change daily settings",'red',attrs=['bold']))
    print(colored("5) ",'white'),colored("Daily",'green',attrs=['bold']))
    print(colored("6) ",'white'),colored("Expedition",'green',attrs=['bold']))
    """
    print(colored("7) ",'white'),colored("GvG",'red',attrs=['bold']))
    print(colored("8) ",'white'),colored("Expedition",'red',attrs=['bold']),colored("  - Funzione semi-manuale!",'cyan',attrs=['bold']))
    print(colored("9) ",'white'),colored("Invasion",'red',attrs=['bold']))
    print(colored("10)",'white'),colored("Debug Mode\n",'green',attrs=['bold']))
    """
    print(f"0)  To close the program\n")
    cprint("Select number: \n",'cyan',attrs=['bold'])
    a = input()
    logging.debug(f'Menu input = {a}')
    if int(a) == 1:
        print(colored("Enter the number of runs: ",'green',attrs=['bold']))
        b = input()
        print(colored("Enter the number:\n",'green',attrs=['bold']),colored("1) normal\n"),colored("2) hard\n"),
              colored("3) heroic\n"),colored("According to the difficulty you want",'green',attrs=['bold']))
        c = input()
        print("Enter the number of how long it takes you to complete a raid run in seconds.\n",
            colored("Be careful not to be precise; It's better to have some more time to prevent the bot from getting stuck",
                    'red',attrs=['bold']))
        d = input()
        if int(c) == 1:
            retraid = RaidClass.raid(b, norm, d)
            logging.debug(f"ritorno del raid = {retraid}")
            return 1
        else:
            if int(c) == 2:
                retraid = RaidClass.raid(b, hard, d)
                logging.debug(f"ritorno del raid = {retraid}")
                return 1
            else:
                if int(c) == 3:
                    retraid = RaidClass.raid(b, hero, d)
                    logging.debug(f"ritorno del raid = {retraid}")
                    return 1
                else:
                    print(colored("Something went wrong with typing the numbers",'red',attrs=['bold']))
                    return 1
    else:
        if int(a) == 2:
            print(colored("ATTENTION: the bot will select the first one in the list by default!\n",'red',attrs=['bold']),
                  colored("Default time: 40 seconds -> if it is too little report it to the developer!",'red',attrs=['bold']))
            cprint("How many pvp runs do you want to do?\n",'green',attrs=['bold'])
            pvprun = input()
            PvPClass.pvp(int(pvprun))
            return 1
        else:
            if int(a) == 3:
                cprint("How many gauntlet runs do you want to do?",'green',attrs=['bold'])
                cimentorun = input()
                cprint("Enter the number of how long it takes you to complete a run in seconds",'green',attrs=['bold'])
                cprint("Be careful not to be precise; It's better to have some more time to prevent the bot from getting stuck",'red',attrs=['bold'])
                timento = input()
                g = GauntletClass.cimento(int(cimentorun), int(timento))
                #if g == 0:
                #    print(colored("Non c'è cimento!",'red',attrs=['bold']))
                return 1
            else:
                if int(a) == 4:
                    setconfig()
                    return 1
                else:
                    if int(a) == 5:
                        cprint("ATTENTION: This command will initiate Raid, Pvp, Trial or Trials of Nynx!",'red',attrs=['bold'])
                        cprint("Make sure you have set the settings of the daily Command 4)",'cyan',attrs=['bold'])
                        print(colored("Press",'cyan',attrs=['bold']),colored("y",'white'),
                              colored("if you are ready to start the daily, otherwise type",'cyan',attrs=['bold']),
                              colored("n",'white'))
                        sure = input()
                        if str(sure)=='y':
                            daily()
                            return 1;
                        else:
                            if str(sure) or int(sure):
                                return 1
                    else:
                        if int(a) == 6:
                            cprint("ATTENTION: This mode requires you to select expedition first!", 'red',
                                   attrs=['bold'])
                            cprint("You have to select which of the 3/4 shipments to make! The BOT will take care of the rest!",
                                   'red', attrs=['bold'])
                            cprint("How many expedition runs do you want to do?",'green',attrs=['bold'])
                            proverun = input()
                            cprint("Enter the number of how long it takes you to complete a run in seconds",'green',attrs=['bold'])
                            cprint("Be careful not to be precise; It's better to have some more time to prevent the bot from getting stuck",'red',attrs=['bold'])
                            promento = input()
                            ExpeditionClass.expedition(int(proverun), promento)
                            return 1;
                        else:
                            cprint("There is no option for this number!", 'red', attrs=['bold'])
                            """
                            if int(a) == 7:
                                cprint("Quante run delle prove di GvG vuoi fare?",'green',attrs=['bold'])
                                gvgrun = input()
                                cprint("Quanto ci impieghi in secondi a finirne uno?", 'green', attrs=['bold'])
                                cprint("Attento: aggiungi del tempo in piu in caso per non impallare il bot!", 'red',
                                       attrs=['bold'])
                                gvgtempo = input()
                                GvG.gvg(int(gvgrun),int(gvgtempo))
                                return 1;
                            else:
                                if int(a)==8 :
                                    cprint("ATTENTO: Questa modalità richiede che tu selezioni prima la spedizione!",'red',attrs=['bold'])
                                    cprint("Devi selezionare te quale delle 3/4 spedizioni fare! Al resto ci pensa il BOT!",'red',attrs=['bold'])
                                    cprint("Quante run desideri fare?",'green',attrs=['bold'])
                                    exprun = input()
                                    cprint("Quanto tempo impieghi a terminare una run?",'green',attrs=['bold'])
                                    cprint("ATTENTO: Aggiungi del tempo in piu onde evitare che si impalli il bot!",'red',attrs=['bold'])
                                    exptime= input()
                                    Expedition.spedizione(int(exprun),int(exptime))
                                    return 1
                                else:
                                    if int(a) == 9:
                                        cprint("Quante run dell'invasione vuoi fare?", 'green', attrs=['bold'])
                                        invrun = input()
                                        cprint("Quanto ci impieghi in secondi a finirne uno?", 'green', attrs=['bold'])
                                        cprint("Attento: aggiungi del tempo in piu in caso per non impallare il bot!",
                                               'red', attrs=['bold'])
                                        invento = input()
                                        Invasion.invasione(int(invrun), invento)
                                        return 1;
                                    else:
                                        if int(a) == 10:
                                            debug()
                                            return 1;
                                        else:
                                            if int(a) == 0:
                                                return 0
                                            else:
                                                cprint("Non esiste un'opzione relativo a questo numero!",'red',attrs=['bold'])
        """

"""
command to edit json file that store information about daily raid etc

"""
def setconfig():
    f = open("data.json", "w")
    cprint("Enter the number of raids you can do daily:",'cyan',attrs=['bold'])
    a = input()
    cprint("For now the difficulty will be preset to heroic for error runtime",'red',attrs=['bold'])
    # diff = input("Inserisci la difficoltà del raid\n")
    cprint("Enter the average time it takes for a raid:",'cyan',attrs=['bold'])
    time = input()
    cprint("Inserisci il numero di run di pvp che puoi fare giornalmente:",'cyan',attrs=['bold'])
    b = input()
    cprint("Enter the number of pvp runs you can do daily:",'cyan',attrs=['bold'])
    c = input()
    cprint("Enter the average time it takes for Gauntlet / Trials:", 'cyan', attrs=['bold'])
    d = input()
    data_dict = {"name": "Utente", "raid": a, "difficolta": hero, "temporaid": time, "pvp": b, "cimento": c, "ctime": d}
    json_test = json.dump(data_dict, f)
    f.close()

"""
Function to do daily task
"""
def daily():
    f = open('data.json', "r")
    data = json.loads(f.read())
    raidshard = int(data['raid'])
    tempo = int(data['temporaid'])
    pvprun = int(data['pvp'])
    cimentorun = int(data['cimento'])
    ctime = int(data['ctime'])
    print(raidshard)
    raid.raid(int(raidshard), hero, int(tempo))
    time.sleep(5)
    PvP.pvp(int(pvprun))
    time.sleep(5)
    # prova a fare cimento. Se ritorna None, ritorna 0
    g = Cimento.cimento(int(cimentorun), int(ctime))
    if g == 0:
        ProveN.prove(int(cimentorun), int(ctime))
    f.close()


def debug():
    print(colored("Debug Mode on. Cerco tutte le immagini",'red'))
    raid = pyautogui.locateCenterOnScreen(r"image\prova.png", grayscale=False,confidence=0.5)
    if raid is not None:
        print(colored("Raid funzionante!",'blue',attrs=['bold']))
    else:
        print(f"Raid = {raid}")
    pvp = pyautogui.locateCenterOnScreen(r"image\pvp.png", grayscale=False,confidence=0.5)
    if pvp is not None:
        print(colored("PvP funzionante!",'blue',attrs=['bold']))
    else:
        print(f"PvP = {pvp}")
    gvg = pyautogui.locateCenterOnScreen(r"image\gvg.png", grayscale=False,confidence=0.5)
    if gvg is not None:
        print(colored("GvG Presente!",'blue',attrs=['bold']))
    else:
        print(f"GvG = {gvg}")
    cimento = pyautogui.locateCenterOnScreen(r"image\cimento.png", grayscale=False,confidence=0.5)
    if cimento is not None:
        print(colored("Cimento presente!",'blue',attrs=['bold']))
    else:
        print(f"Cimento = {cimento}")
    prove = pyautogui.locateCenterOnScreen(r"image\prove.png", grayscale=False,confidence=0.5)
    if prove is not None:
        print(colored("Prove presente!",'blue',attrs=['bold']))
    else:
        print(f"Prove di Nyxn = {prove}")
    invasione = pyautogui.locateCenterOnScreen(r"image\invasione.png", grayscale=False, confidence=0.5)
    if invasione is not None:
        print(colored("Invasione presente!", 'blue', attrs=['bold']))
    else:
        print(f"Invasione = {invasione}")
    print(colored("\nNel caso ci fossero dei None, assicurati che siano disponibili, in tal caso spostati",'red',attrs=['bold']))
    time.sleep(5)
    return 1;


def main():
    logging.basicConfig(filename="latest.log", filemode="w", format='%(asctime)s - %(funcName)s :   %(message)s', level=logging.DEBUG)
    logging.info(f"VERSION : {VERSION} - BOT by HoloKi. Info : https://github.com/HoloKi/BitHeroesBot")
    logging.info("https://discord.gg/h98xsssEpe")
    logging.info("The bot is completely free, any sale is prohibited.If someone sold it to you, get your money back and report it to the developer")
    ciclo = 1
    print(f"BitHeroesBot by Holoki ------ VERSION = {VERSION} ------ Translate by PastShadie")
    print("All info on latest.log")
    while True:
        ciclo = menu()
        if ciclo == 0:
            exit()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.error(e)
