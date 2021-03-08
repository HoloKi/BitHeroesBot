import pyautogui
import time
import json
import cv2 as cv
import logging
import raid
import Cimento
import PvP
import ProveN
import GvG
from colorama import *
from termcolor import colored,cprint

init(autoreset=True); #Permette ad ogni print di ritornare al suo colore base

VERSION = 3.1

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
    print(colored("7) ",'white'),colored("GvG",'green',attrs=['bold']))
    print(colored("10)",'white'),colored("Debug Mode\n",'green',attrs=['bold']))
    print(f"0)Per chiudere il programma\n")
    a = input("Seleziona numero: \n")
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
            retraid = raid.raid(b, norm, d)
            logging.debug(f"ritorno del raid = {retraid}")
            return 1
        else:
            if int(c) == 2:
                retraid = raid.raid(b, hard, d)
                logging.debug(f"ritorno del raid = {retraid}")
                return 1
            else:
                if int(c) == 3:
                    retraid = raid.raid(b, hero, d)
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
                if g == 0:
                    print(colored("Non c'è cimento!",'red',attrs=['bold']))
                return 1
            else:
                if int(a) == 4:
                    setconfig()
                    return 1
                else:
                    if int(a) == 5:
                        daily()
                        return 1
                    else:
                        if int(a) == 6:
                            cprint("Quante run delle prove di Nynx vuoi fare?\n",'green',attrs=['bold'])
                            proverun = input()
                            cprint("Quanto ci impieghi in secondi a finirne uno?",'green',attrs=['bold'])
                            cprint("Attento: aggiungi del tempo in piu in caso per non impallare il bot!\n",'red',attrs=['bold'])
                            promento = input()
                            ProveN.prove(int(proverun), promento)
                            return 1;
                        else:
                            if int(a) == 7:
                                gvgrun = input("Quante run delle prove di GvG vuoi fare?\n")
                                gvgtempo = input("Quanto ci impieghi in secondi a finirne uno?\n "
                                                 "Aggiungi del tempo in piu in caso!\n")
                                GvG.gvg(int(gvgrun),int(gvgtempo))
                                return 1;
                            else:
                                if int(a) == 10:
                                    debug()
                                    return 1;
                                else:
                                    if int(a) == 0:
                                        return 0
                                    else:
                                        print("Non esiste un'opzione relativo a questo numero!")


def test(name, numero):
    raidcord = pyautogui.locateCenterOnScreen(name, grayscale=False, confidence=numero)
    print(raidcord)
    pyautogui.click(raidcord)
    return raidcord


# potrei fare def setconfig(a,b,c)
def setconfig():
    f = open("data.json", "w")
    a = input("Inserisci il numero di raid che puoi fare giornalmente\n")
    print("Per ora la difficoltà sarà preimpostata su eroico per error runtime\n")
    # diff = input("Inserisci la difficoltà del raid\n")
    time = input("Inserisci il tempo medio che impieghi per un raid\n")
    b = input("Inserisci il numero di run di pvp che puoi fare giornalmente\n")
    c = input("Inserisci il numero di run di cimento che puoi fare giornalmente\n")
    data_dict = {"name": "Utente", "raid": a, "difficolta": hero, "temporaid": time, "pvp": b, "cimento": c}
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
    print(raidshard)
    raid.raid(int(raidshard), hero, int(tempo))
    time.sleep(5)
    PvP.pvp(int(pvprun))
    time.sleep(5)
    # prova a fare cimento. Se ritorna None, ritorna 0
    g = Cimento.cimento(int(cimentorun), 200)
    if g == 0:
        ProveN.prove(int(cimentorun), 200)
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
    if raid is not None:
        print(colored("Prove presente!",'blue',attrs=['bold']))
    else:
        print(f"Prove di Nyxn = {prove}")
    print(colored("\nNel caso ci fossero dei None, assicurati che siano disponibili, in tal caso spostati",'red',attrs=['bold']))
    time.sleep(5)
    return 1;


def main():
    logging.basicConfig(filename="latest.log", filemode="w", format='%(asctime)s - %(funcName)s :   %(message)s', level=logging.DEBUG)
    logging.info(f"VERSION : {VERSION} - BOT by HoloKi. Info : https://github.com/HoloKi/BitHeroesBot")
    ciclo = 1
    print(f"BitHeroesBot by Holoki ------ VERSION = {VERSION}. All info on latest.log")
    while True:
        ciclo = menu()
        if ciclo == 0:
            exit()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.error(e)
