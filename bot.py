import pyautogui
import time
import json
import cv2 as cv
import logging
import RaidClass
import Cimento
import PvP
import ProveN
import GvG
import Expedition
import Invasion
from colorama import *
from termcolor import colored,cprint
import asyncio

init(autoreset=True); #Permette ad ogni print di ritornare al suo colore base

VERSION = "5.0.1"

hero = "heroic"
hard = "hard"
norm = "normal"

def menu():
    print("\n\n")
    print(colored("Digita il numero per selezionare l'opzione desiderato:\n",'red',attrs=['bold']))
    print(colored("1) ",'white'),colored("Raid",'green',attrs=['bold']))
    print(colored("2) ",'white'),colored("Pvp",'green',attrs=['bold']))
    print(colored("3) ",'white'),colored("Cimento",'green',attrs=['bold']))
    print(colored("4) ",'white'),colored("Cambiare impostazioni delle daily",'red',attrs=['bold']))
    print(colored("5) ",'white'),colored("Daily",'green',attrs=['bold']))
    print(colored("6) ",'white'),colored("Prove di Nynx",'green',attrs=['bold']))
    print(colored("7) ",'white'),colored("GvG",'red',attrs=['bold']))
    print(colored("8) ",'white'),colored("Spedizione",'red',attrs=['bold']),colored("  - Funzione semi-manuale!",'cyan',attrs=['bold']))
    print(colored("9) ",'white'),colored("Invasione",'red',attrs=['bold']))
    print(colored("10)",'white'),colored("Debug Mode\n",'green',attrs=['bold']))
    print(f"0) Per chiudere il programma\n")
    cprint("Seleziona numero: \n",'cyan',attrs=['bold'])
    a = input()
    logging.debug(f'Menu input = {a}')
    if int(a) == 1:
        print(colored("Digita il numero di run: ",'green',attrs=['bold']))
        b = input()
        print(colored("Digita il numero:\n",'green',attrs=['bold']),colored("1) normal\n"),colored("2) hard\n"),
              colored("3) heroic\n"),colored("In base alla difficoltà che desideri",'green',attrs=['bold']))
        c = input()
        print("Digita il numero relativo a quanto impieghi a completare una run del raid in secondi.\n",
            colored("Attento: non essere preciso, meglio avere del tempo in piu per evitare che il bot si impalli",
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
                    print(colored("Qualcosa è andato storto con la digitazione dei numeri",'red',attrs=['bold']))
                    return 1
    else:
        if int(a) == 2:
            print(colored("ATTENTO: il bot selezionerà di default il primo nella lista!\n",'red',attrs=['bold']),
                  colored("Tempo default: 40 secondi -> se è troppo poco segnalalo allo sviluppatore!",'red',attrs=['bold']))
            cprint("Quante run di pvp vuoi fare?\n",'green',attrs=['bold'])
            pvprun = input()
            PvP.pvp(int(pvprun))
            return 1
        else:
            if int(a) == 3:
                cprint("Quante run del cimento vuoi fare?",'green',attrs=['bold'])
                cimentorun = input()
                cprint("Quanto tempo impieghi in secondi a finire una run?",'green',attrs=['bold'])
                cprint("Attento: aggiungi del tempo in piu per non impallare il bot!",'red',attrs=['bold'])
                timento = input()
                g = Cimento.cimento(int(cimentorun), int(timento))
                #if g == 0:
                #    print(colored("Non c'è cimento!",'red',attrs=['bold']))
                return 1
            else:
                if int(a) == 4:
                    setconfig()
                    return 1
                else:
                    if int(a) == 5:
                        cprint("ATTENTO: Questo comando avvierà Raid, Pvp, Cimento o Prove di Nynx!",'red',attrs=['bold'])
                        cprint("Assicurati di aver settato per bene le impostazioni delle daily Comando 4)",'cyan',attrs=['bold'])
                        print(colored("Premi",'cyan',attrs=['bold']),colored("y",'white'),
                              colored("se sei pronto per startare le daily, altrimenti digita",'cyan',attrs=['bold']),
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
                            cprint("Quante run delle prove di Nynx vuoi fare?",'green',attrs=['bold'])
                            proverun = input()
                            cprint("Quanto ci impieghi in secondi a finirne uno?",'green',attrs=['bold'])
                            cprint("Attento: aggiungi del tempo in piu in caso per non impallare il bot!",'red',attrs=['bold'])
                            promento = input()
                            ProveN.prove(int(proverun), promento)
                            return 1;
                        else:
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
                                    cprint("Devi selezionare te quale delle 4 spedizioni fare! Al resto ci pensa il BOT!",'red',attrs=['bold'])
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


def test(name, numero):
    raidcord = pyautogui.locateCenterOnScreen(name, grayscale=False, confidence=numero)
    print(raidcord)
    pyautogui.click(raidcord)
    return raidcord

# potrei fare def setconfig(a,b,c)
def setconfig():
    f = open("data.json", "w")
    cprint("Inserisci il numero di raid che puoi fare giornalmente:",'cyan',attrs=['bold'])
    a = input()
    cprint("Per ora la difficoltà sarà preimpostata su eroico per error runtime\n",'red',attrs=['bold'])
    # diff = input("Inserisci la difficoltà del raid\n")
    cprint("Inserisci il tempo medio che impieghi per un raid:",'cyan',attrs=['bold'])
    time = input()
    cprint("Inserisci il numero di run di pvp che puoi fare giornalmente:",'cyan',attrs=['bold'])
    b = input()
    cprint("Inserisci il numero di run di Cimento/Prove che puoi fare giornalmente:",'cyan',attrs=['bold'])
    c = input()
    cprint("Inserisci il tempo medio che impieghi per Cimento/Prove:", 'cyan', attrs=['bold'])
    d = input()
    data_dict = {"name": "Utente", "raid": a, "difficolta": hero, "temporaid": time, "pvp": b, "cimento": c, "ctime": d}
    json_test = json.dump(data_dict, f)
    # test_dict = {"name": "Arty", "test": "funziona"}
    # json.dump(test_dict,f)
    f.close()


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
    ciclo = 1
    print(f"BitHeroesBot by Holoki ------ VERSION = {VERSION}. All info on latest.log")
    print(f"Translate - PastShadie")
    while True:
        ciclo = menu()
        if ciclo == 0:
            exit()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.error(e)
