import pyautogui
import time
import json
import cv2 as cv
import logging

VERSION = 2.2

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
    print(f"0)Per chiudere il programma\n")
    a = input("Seleziona numero: \n")
    logging.debug(f'Menu input = {a}')
    if int(a) == 1:
        b = input("Digita il numero di run: \n")
        c = input("Digita 1)normal 2)hard 3)heroic in base alla difficoltà che desideri\n")
        d = input(
            "Digita il numero relativo a quanto impieghi a completare una run del raid in secondi.\n Attento, non essere preciso, meglio avere del tempo in piu per eventuali\n")
        if int(c) == 1:
            retraid = raid(b, norm, d)
            logging.debug(f"ritorno del raid = {retraid}")
            return 1
        else:
            if int(c) == 2:
                retraid = raid(b, hard, d)
                logging.debug(f"ritorno del raid = {retraid}")
                return 1
            else:
                if int(c) == 3:
                    retraid = raid(b, hero, d)
                    logging.debug(f"ritorno del raid = {retraid}")
                    return 1
                else:
                    print("Qualcosa è andato storto con la digitazione dei numeri")
                    return 1
    else:
        if int(a) == 2:
            pvprun = input(
                "Quante run di pvp vuoi fare?\n ATTENTO: il bot selezionera di default il primo nella lista! \n")
            pvp(int(pvprun))
            return 1
        else:
            if int(a) == 3:
                cimentorun = input("Quante run di cimento vuoi fare?\n")
                timento = input("Quanto ci impieghi in secondi a finirne uno?\n Aggiungi del tempo in piu in caso!\n")
                g = cimento(int(cimentorun), int(timento))
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
                            prove(int(proverun), promento)
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


# run = numero di shard
# difficult = difficoltà
# duration = quanto dura in secondi una run
#ritorna 1 se tutto va bene, in caso 0. il break va solo nel ciclo while
def raid(run, difficult, duration):
    conta = 1
    print("\nRAID\n")
    print(f"run = {run}, difficolta = {difficult} e durata = {duration} secondi\n")
    logging.debug(f"run = {run}, difficoltà = {difficult}, durata = {duration}")
    time.sleep(3)
    #caso in cui le run sono minori di 1, ritorna 0
    if int(run) < 1:
        logging.debug("duration < 1")
        pyautogui.alert(text='the number of raid runs must be 1 or greater', button='OK')
        return 0
    else:
        raidcord = pyautogui.locateCenterOnScreen("prova.png", grayscale=False, confidence=0.6)
        logging.debug(f"raid button = {raidcord}. If None, to fix it, change position in the screen.")
        if raidcord is not None:
            pyautogui.click(raidcord)
            time.sleep(2)
            shardcheck = pyautogui.locateCenterOnScreen("noshard.png", grayscale=False, confidence=0.9)
            logging.debug(f"shardcheck = {shardcheck}. if None its ok!")
            if shardcheck is None:
                evoca = pyautogui.locateCenterOnScreen("startraid.png", grayscale=False, confidence=0.5)
                logging.debug(f"evoca = {evoca}.")
                if evoca is not None:
                    pyautogui.click(evoca)
                    time.sleep(3)
                    if difficult == hero:
                        difficulty = pyautogui.locateCenterOnScreen("eroic.png", grayscale=False, confidence=0.4)
                    if difficult == hard:
                        difficulty = pyautogui.locateCenterOnScreen("hard.png", grayscale=False, confidence=0.5)
                    if difficult == norm:
                        difficulty = pyautogui.locateCenterOnScreen("normal.png", grayscale=False, confidence=0.5)
                    #if difficult != norm and difficult != hard and difficult != hero:
                    #    print("error")
                    #    log("difficult error, probably not norm,hard or hero", "a")
                    #    exit()
                    logging.debug(f"difficult = {difficulty}.")
                    if difficulty is not None:
                        pyautogui.click(difficulty)
                        time.sleep(2)
                        accept = pyautogui.locateCenterOnScreen("accept.png", grayscale=False, confidence=0.5)
                        logging.debug(f"accept = {accept}")
                        if accept is not None:
                            pyautogui.click(accept)
                            # tempo dedicato al completamento del raid in auto
                            while True:
                                print(f"giro numero = {conta}")
                                time.sleep(int(duration))
                                if int(run) == 1:
                                    yes = pyautogui.locateCenterOnScreen("yes.png", grayscale=False, confidence=0.5)
                                    logging.debug(f"yes = {yes}")
                                    time.sleep(3)
                                    if yes is not None:
                                        pyautogui.click(yes)
                                        time.sleep(5)
                                        xbutton = pyautogui.locateCenterOnScreen("xbutton.png", grayscale=False, confidence=0.5)
                                        logging.debug(f"xbutton = {xbutton}")
                                        pyautogui.click(xbutton)
                                        break
                                    else:
                                        print("Tempo impostato non sufficiente!")
                                        return 0

                                else:
                                    conta = int(conta) + 1
                                    run = int(run) - 1
                                    rerun = pyautogui.locateCenterOnScreen("rerun.png", grayscale=False, confidence=0.5)
                                    logging.debug(f"rerun = {rerun}")
                                    time.sleep(3)
                                    pyautogui.click(rerun)
                            return 1

                        else:
                            print("Tasto accept non trovato!\n")
                            logging.error("AcceptError, please send this to github issue")
                            print("Please report this bug/error on github\n")
                            return 0
                    else:
                        print("Tasto della difficolta non trovato!\n")
                        logging.error("Difficult error, please send this to github issue")
                        print("Please report this bug/error on github\n")
                        return 0
                else:
                    print("Tasto evoca non trovato!r\n")
                    logging.debug("Evoca is none, please send this to github issue")
                    print("Please report this bug/error on github\n")
                    return 0
            else:
                print("Shard non disponibili!\n")
                logging.debug("No shard")
                time.sleep(5)
                xbutton = pyautogui.locateCenterOnScreen("xbutton.png", grayscale=False, confidence=0.5)
                logging.debug(f"xbutton = {xbutton}")
                pyautogui.click(xbutton)
        else:
            print("Tasto errore non trovato!\n")
            logging.debug("Raid is None,please report this error on github")
            print("Prova a spostarti un pochino e riprova il comando!\n")
            return 0


def pvp(run):
    conta = 1
    logging.debug(f"run = {run}")
    print("\n-----PVP-----\n")
    print(f"run = {run}\n")
    if run <= 0:
        pyautogui.alert(text="Run must be > 0", button="OK")
        logging.debug("run < 1")
        exit()
    pvp = pyautogui.locateCenterOnScreen("pvp.png", grayscale=False, confidence=0.5)
    logging.debug(f"pvp button = {pvp}")
    if pvp is not None:
        pyautogui.click(pvp)
        while True:
            time.sleep(2)
            play = pyautogui.locateCenterOnScreen("play.png", grayscale=False, confidence=0.5)
            logging.debug(f"play = {play}")
            if play is not None:
                pyautogui.click(play)
                time.sleep(2)
                battle = pyautogui.locateCenterOnScreen("battle1.png", grayscale=False, confidence=0.5)
                logging.debug(f"battle = {battle}")
                if battle is not None:
                    pyautogui.click(battle)
                    time.sleep(2)
                    accept = pyautogui.locateCenterOnScreen("accept.png", grayscale=False, confidence=0.5)
                    logging.debug(f"battle = {battle}")
                    if accept is not None:
                        pyautogui.click(accept)
                        print(f"giro numero = {conta}")
                        time.sleep(100)
                        conta = int(conta) + 1
                        close = pyautogui.locateCenterOnScreen("close.png", grayscale=False, confidence=0.5)
                        logging.debug(f"close = {close}")
                        if close is not None:
                            pyautogui.click(close)
                            time.sleep(2)
                            run = int(run) - 1
                            if int(run) == 0:
                                xbutton = pyautogui.locateCenterOnScreen("xbutton.png", grayscale=False, confidence=0.5)
                                logging.debug(f"xbutton = {xbutton}")
                                if xbutton is not None:
                                    pyautogui.click(xbutton)
                                    break
                                else:
                                    logging.error("log button is None")
                                    print("Please report this bug/error on github")
                                    break
                        else:
                            logging.error("close is None")
                            print("Please report this bug/error on github")
                            break
                    else:
                        logging.error("accept is None")
                        print("Please report this bug/error on github")
                        break
                else:
                    logging.error("battle is None")
                    print("Please report this bug/error on github")
                    break
            else:
                logging.error("play is None")
                print("Please report this bug/error on github")
                break
        return 1
    else:
        logging.error(f"problem with pvp.png. pvp = {pvp}")
        print("Please report this bug/error on github")


def cimento(run, tempo):
    logging.debug(f"run = {run}, time = {tempo} seconds")
    print("CIMENTO")
    if run <= 0:
        logging.debug("run < 1")
        pyautogui.alert(text="Run must be > 0", button="OK")
        exit(0)
    cimento = pyautogui.locateCenterOnScreen("cimento.png", grayscale=False, confidence=0.5)
    logging.debug(f"cimento button = {cimento}")
    if cimento is not None:
        pyautogui.click(cimento)
        while True:
            time.sleep(3)
            play = pyautogui.locateCenterOnScreen("play.png", grayscale=False, confidence=0.5)
            logging.debug(f"play = {play}")
            if play is not None:
                pyautogui.click(play)
                time.sleep(3)
                accept = pyautogui.locateCenterOnScreen("accept.png", grayscale=False, confidence=0.5)
                logging.debug(f'accept = {play}')
                if accept is not None:
                    pyautogui.click(accept)
                    time.sleep(int(tempo))
                    close = pyautogui.locateCenterOnScreen("close.png", grayscale=False, confidence=0.5)
                    logging.debug(f'close = {close}')
                    if close is not None:
                        pyautogui.click(close)
                        time.sleep(3)
                        run = int(run) - 1
                        if int(run) == 0:
                            xbutton = pyautogui.locateCenterOnScreen("xbutton.png", grayscale=False, confidence=0.5)
                            if xbutton is not None:
                                pyautogui.click(xbutton)
                                break
                            else:
                                logging.debug(f'close = {close}')
                                print("Please report this bug/error on github")
                                break
                    else:
                        logging.error("close is None")
                        print("Please report this bug/error on github")
                        break
                else:
                    logging.error("accept is None")
                    print("Please report this bug/error on github")
                    break
            else:
                logging.error("play is None")
                print("Please report this bug/error on github")
                break
    else:
        logging.error(f'problem with cimento.png. return = {cimento}')
        print("Non trovo cimento o non funziona")
        return 0


def prove(run, tempo):
    print("\nPROVE\n")
    print(f"run = {run}, tempo per un completamento = {tempo}\n")
    conta = 1
    logging.debug(f"run = {run}, time = {tempo}")
    if run <= 0:
        logging.debug("Run < 1")
        pyautogui.alert(text="Run must be > 0", button="OK")
        exit(0)
    provebutton = pyautogui.locateCenterOnScreen("prove.png", grayscale=False, confidence=0.5)
    logging.debug(f"bottone prove = {provebutton}")
    if provebutton is not None:
        pyautogui.click(provebutton)
        while True:
            time.sleep(3)
            play = pyautogui.locateCenterOnScreen("play.png", grayscale=False, confidence=0.5)
            logging.debug(f"play = {play}")
            if play is not None:
                pyautogui.click(play)
                time.sleep(3)
                accept = pyautogui.locateCenterOnScreen("accept.png", grayscale=False, confidence=0.5)
                logging.debug(f"accept = {accept}")
                if accept is not None:
                    pyautogui.click(accept)
                    print(f"giro numero = {conta}")
                    time.sleep(int(tempo))
                    close = pyautogui.locateCenterOnScreen("close.png", grayscale=False, confidence=0.5)
                    logging.debug(f"close = {close}")
                    if close is not None:
                        pyautogui.click(close)
                        time.sleep(5)
                        run = int(run) - 1
                        conta = int(conta) + 1
                        if int(run) == 0:
                            xbutton = pyautogui.locateCenterOnScreen("xbutton.png", grayscale=False, confidence=0.5)
                            if xbutton is not None:
                                pyautogui.click(xbutton)
                                break
                            else:
                                logging.debug(f"close = {close}")
                                print("Please report this bug/error on github")
                                break
                    else:
                        logging.debug("close is None")
                        print("Please report this bug/error on github")
                        break
                else:
                    logging.debug("accept is None")
                    print("Please report this bug/error on github")
                    break
            else:
                logging.debug("play is None")
                print("Please report this bug/error on github")
                break
    else:
        logging.debug(f"problem with prove.png. return = {provebutton} ")
        print("Please report this bug/error on github")
        return 0


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
    raid(int(raidshard), hero, int(tempo))
    time.sleep(5)
    pvp(int(pvprun))
    time.sleep(5)
    # prova a fare cimento. Se ritorna None, ritorna 0
    g = cimento(int(cimentorun), 200)
    if g == 0:
        prove(int(cimentorun), 200)
    f.close()


def main():
    logging.basicConfig(filename="latest.log", filemode="w", format='%(asctime)s - %(funcName)s :   %(message)s', level=logging.DEBUG)
    logging.info(f"VERSION : {VERSION} - BOT by HoloKi. Info : https://github.com/HoloKi/BitHeroesBot")
    ciclo = 1
    # a = input("inserisci il numero di run del raid: \n")
    # b = input("inserisci il la difficoltà del raid scrivendo norm = normal, hard = hard o hero = heroic\n ")
    # print(b)
    # c = input("Inserisci il tempo impiegato per finire una run(in secondi). Attento...meglio dare qualche secondo in piu! \n")
    # Raid(a,str(b),c)
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
