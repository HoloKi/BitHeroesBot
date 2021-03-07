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

VERSION = 2.4

hero = "heroic"
hard = "hard"
norm = "normal"

def menu():
    print("\n\n\n")
    print(f"Digita il numero per selezionare l'opzione desiderato\n")
    print(f"1)Per utilizzare la funzione raid\n")
    print(f"2)Per utilizzare la funzione pvp\n")
    print(f"3)Per utilizzare la funzione cimento\n")
    print(f"4)Per modificare le impostazioni delle daily\n")
    print(f"5)Per utilizzare la funzione daily\n")
    print(f"6)Per utilizzare la funzione prova\n")
    print(f"7)Per utilizzare la funzione gvg\n")
    print(f"0)Per chiudere il programma\n")
    a = input("Seleziona numero: \n")
    logging.debug(f'Menu input = {a}')
    if int(a) == 1:
        b = input("Digita il numero di run: \n")
        c = input("Digita 1)normal 2)hard 3)heroic in base alla difficoltà che desideri\n")
        d = input(
            "Digita il numero relativo a quanto impieghi a completare una run del raid in secondi.\n Attento, non essere preciso, meglio avere del tempo in piu per eventuali\n")
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
                    print("Qualcosa è andato storto con la digitazione dei numeri")
                    return 1
    else:
        if int(a) == 2:
            pvprun = input(
                "Quante run di pvp vuoi fare?\n ATTENTO: il bot selezionera di default il primo nella lista! \n")
            PvP.pvp(int(pvprun))
            return 1
        else:
            if int(a) == 3:
                cimentorun = input("Quante run di cimento vuoi fare?\n")
                timento = input("Quanto ci impieghi in secondi a finirne uno?\n Aggiungi del tempo in piu in caso!\n")
                g = Cimento.cimento(int(cimentorun), int(timento))
                if g == 0:
                    print("Non c'è cimento!")
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
                            proverun = input("Quante run delle prove di Nynx vuoi fare?\n")
                            promento = input("Quanto ci impieghi in secondi a finirne uno?\n "
                                             "Aggiungi del tempo in piu in caso!\n")
                            ProveN.prove(int(proverun), promento)
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
    pvp(int(pvprun))
    time.sleep(5)
    # prova a fare cimento. Se ritorna None, ritorna 0
    g = Cimento.cimento(int(cimentorun), 200)
    if g == 0:
        ProveN.prove(int(cimentorun), 200)
    f.close()


def main():
    logging.basicConfig(filename="latest.log", filemode="w", format='%(asctime)s - %(funcName)s :   %(message)s', level=logging.DEBUG)
    logging.info(f"VERSION : {VERSION} - BOT by HoloKi. Info : https://github.com/HoloKi/BitHeroesBot")
    ciclo = 1
    print("Start")
    while True:
        ciclo = menu()
        if ciclo == 0:
            exit()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.error(e)
