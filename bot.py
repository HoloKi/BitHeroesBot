import pyautogui
import time
from datetime import datetime
import json


def log(message, modo):
    f = open("log.txt", modo)
    f.write(str(message))
    f.write("\n")
    f.close()


hero = "heroic"
hard = "hard"
norm = "normal"


def menu():
    print("\n\n\n\n\n")
    print(f"Digita il numero per selezionare l'opzione desiderato\n")
    print(f"1)Per utilizzare la funzione Raid\n")
    print(f"2)Per utilizzare la funzione raid\n")
    print(f"3)Per utilizzare la funzione cimento\n")
    print(f"4)Per modificare le impostazioni delle daily\n")
    print(f"5)Per autilizzare la funzione daily\n")
    print(f"6)PEr utilizzare la funzione prova")
    print(f"0)Per chiudere il programma\n")
    a = input("Seleziona numero: \n")
    if int(a) == 1:
        b = input("Digita il numero di run: \n")
        c = input("Digita 1)normal 2)hard 3)heroic in base alla difficoltà che desideri\n")
        d = input(
            "Digita il numero relativo a quanto impieghi a completare una run del raid in secondi.\n Attento, non essere preciso, meglio avere del tempo in piu per eventuali\n")
        if int(c) == 1:
            raid(b, norm, d)
            return 1
        else:
            if int(c) == 2:
                raid(b, hard, d)
                return 1
            else:
                if int(c) == 3:
                    raid(b, hero, d)
                    return 1
                else:
                    print("Qualcosa è andato storto con la digitazione dei numeri")
                    return 1
    else:
        if int(a) == 2:
            pvprun = input(
                "Quante run di pvp vuoi fare?\n ATTENTO:il bot selezioneràdi default il primo nella lista! \n")
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
                            proverun = input("!uante run delle prove di Nynx vuoi fare?\n")
                            promento = input("Quanto ci impieghi in secondi a finirne uno?\n Aggiungi del tempo in piu in caso!\n")
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
def raid(run, difficult, duration):
    print("RAID")
    log(f"{difficult},{duration}", "a")
    log("raid", "a")
    time.sleep(3)
    if int(run) < 1:
        log("run<1", "a")
        pyautogui.alert(text='the number of raid runs must be 1 or greater', button='OK')
        exit()
    else:
        log("run: ", "a")
        log(run, "a")
        shardcheck = pyautogui.locateCenterOnScreen("noshard.png", grayscale=False, confidence=0.5)
        if shardcheck is not None:
            raidcord = pyautogui.locateCenterOnScreen("prova.png", grayscale=False, confidence=0.7)
            log(raidcord, "a")
            if raidcord is not None:
                pyautogui.click(raidcord)
                time.sleep(2)
                evoca = pyautogui.locateCenterOnScreen("startraid.png", grayscale=False, confidence=0.5)
                log("evoca: ", "a")
                log(evoca, "a")
                if evoca is not None:
                    pyautogui.click(evoca)
                    time.sleep(3)
                    if difficult == hero:
                        difficulty = pyautogui.locateCenterOnScreen("eroic.png", grayscale=False, confidence=0.4)
                        print(difficulty)
                    if difficult == hard:
                        difficulty = pyautogui.locateCenterOnScreen("hard.png", grayscale=False, confidence=0.5)
                        print(difficulty)
                    if difficult == norm:
                        difficulty = pyautogui.locateCenterOnScreen("normal.png", grayscale=False, confidence=0.5)
                        print(difficulty)
                    #if difficult != norm and difficult != hard and difficult != hero:
                    #    print("error")
                    #    log("difficult error, probably not norm,hard or hero", "a")
                    #    exit()
                    log("difficulty: ", "a")
                    log(difficulty, "a")
                    if difficulty is not None:
                        pyautogui.click(difficulty)
                        time.sleep(2)
                        accept = pyautogui.locateCenterOnScreen("accept.png", grayscale=False, confidence=0.5)
                        log("accept: ", "a")
                        log(accept, "a")
                        if accept is not None:
                            pyautogui.click(accept)
                            # tempo dedicato al completamento del raid in auto
                            time.sleep(int(duration))
                            while True:
                                if int(run) == 1:
                                    print(f"run debug = {run}")
                                    yes = pyautogui.locateCenterOnScreen("yes.png", grayscale=False, confidence=0.5)
                                    log("yes: ", "a")
                                    log(yes, "a")
                                    time.sleep(3)
                                    pyautogui.click(yes)
                                    time.sleep(3)
                                    xbutton = pyautogui.locateCenterOnScreen("xbutton.png", grayscale=False, confidence=0.5)
                                    pyautogui.click(xbutton)
                                    time.sleep(3)
                                    xbutton = pyautogui.locateCenterOnScreen("xbutton.png", grayscale=False, confidence=0.5)
                                    pyautogui.click(xbutton)
                                    break
                                else:
                                    print(f"run debug = {run}")
                                    run = int(run) - 1
                                    rerun = pyautogui.locateCenterOnScreen("rerun.png", grayscale=False, confidence=0.5)
                                    log("rerun: ", "a")
                                    log(rerun, "a")
                                    time.sleep(3)
                                    pyautogui.click(rerun)
                                    time.sleep(int(duration))
                        else:
                            print("AcceptError\n")
                            log("Accept is None", "a")
                            print("Please report this bug/error on github\n")
                            exit()
                    else:
                        print("DifficultError\n")
                        log("Difficult is None", "a")
                        print("Please report this bug/error on github\n")
                        exit()
                else:
                    print("EvocaError\n")
                    log("Evoca is none", "a")
                    print("Please report this bug/error on github")
                    exit()
            else:
                print("RaidError\n")
                log("Raid is None", "a")
                print("Please report this bug/error on github")
                exit()
        else:
            print("Shard non disponibili!")
            log("No shard", "a")


def pvp(run):
    print("PVP")
    log("--------pvp----------", "a")
    log("run: ", "a")
    log(run, "a")
    if run <= 0:
        pyautogui.alert(text="Run must be > 0", button="OK")
        exit()
    pvp = pyautogui.locateCenterOnScreen("pvp.png", grayscale=False, confidence=0.5)
    log("pvpbutton: ", "a")
    log(pvp, "a")
    if pvp is not None:
        pyautogui.click(pvp)
        while True:
            time.sleep(2)
            play = pyautogui.locateCenterOnScreen("play.png", grayscale=False, confidence=0.5)
            log("play: ", "a")
            log(play, "a")
            if play is not None:
                pyautogui.click(play)
                time.sleep(2)
                battle = pyautogui.locateCenterOnScreen("battle1.png", grayscale=False, confidence=0.5)
                log("battle: ", "a")
                log(battle, "a")
                if battle is not None:
                    pyautogui.click(battle)
                    time.sleep(2)
                    accept = pyautogui.locateCenterOnScreen("accept.png", grayscale=False, confidence=0.5)
                    log("accept: ", "a")
                    log(accept, "a")
                    if accept is not None:
                        pyautogui.click(accept)
                        time.sleep(100)
                        close = pyautogui.locateCenterOnScreen("close.png", grayscale=False, confidence=0.5)
                        log("close: ", "a")
                        log(close, "a")
                        if close is not None:
                            pyautogui.click(close)
                            time.sleep(2)
                            run = int(run) - 1
                            if int(run) == 0:
                                xbutton = pyautogui.locateCenterOnScreen("xbutton.png", grayscale=False, confidence=0.5)
                                if xbutton is not None:
                                    pyautogui.click(xbutton)
                                    break
                                else:
                                    log("log button is None", "a")
                                    print("Please report this bug/error on github")
                                    break
                        else:
                            log("close is None", "a")
                            print("Please report this bug/error on github")
                            break
                    else:
                        log("accept is None", "a")
                        print("Please report this bug/error on github")
                        break
                else:
                    log("battle is None", "a")
                    print("Please report this bug/error on github")
                    break
            else:
                log("play is None", "a")
                print("Please report this bug/error on github")
                break
    else:
        log("problem with pvp.png. return = ", "a")
        log(pvp, "a")
        print("Please report this bug/error on github")


def cimento(run, tempo):
    print("CIMENTO")
    log("--------cimento----------", "a")
    log("run: ", "a")
    log(run, "a")
    if run <= 0:
        pyautogui.alert(text="Run must be > 0", button="OK")
        exit(0)
    cimento = pyautogui.locateCenterOnScreen("cimento.png", grayscale=False, confidence=0.5)
    log("cimentobutton: ", "a")
    log(cimento, "a")
    if cimento is not None:
        pyautogui.click(cimento)
        while True:
            time.sleep(3)
            play = pyautogui.locateCenterOnScreen("play.png", grayscale=False, confidence=0.5)
            log("play: ", "a")
            log(play, "a")
            if play is not None:
                pyautogui.click(play)
                time.sleep(3)
                accept = pyautogui.locateCenterOnScreen("accept.png", grayscale=False, confidence=0.5)
                log("accept: ", "a")
                log(accept, "a")
                if accept is not None:
                    pyautogui.click(accept)
                    time.sleep(int(tempo))
                    close = pyautogui.locateCenterOnScreen("close.png", grayscale=False, confidence=0.5)
                    log("close: ", "a")
                    log(close, "a")
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
                                log(close, "a")
                                print("Please report this bug/error on github")
                                break
                    else:
                        log("close is None", "a")
                        print("Please report this bug/error on github")
                        break
                else:
                    log("accept is None", "a")
                    print("Please report this bug/error on github")
                    break
            else:
                log("play is None", "a")
                print("Please report this bug/error on github")
                break
    else:
        log("problem with cimento.png. return = ", "a")
        log(cimento, "a")
        print("Non trovo cimento o non funziona")
        return 0


def prove(run, tempo):
    print("PROVE")
    log("--------prove----------", "a")
    log("run: ", "a")
    log(run, "a")
    if run <= 0:
        pyautogui.alert(text="Run must be > 0", button="OK")
        exit(0)
    provebutton = pyautogui.locateCenterOnScreen("prove.png", grayscale=False, confidence=0.5)
    log("provebutton: ", "a")
    log(provebutton, "a")
    if provebutton is not None:
        pyautogui.click(provebutton)
        while True:
            time.sleep(3)
            play = pyautogui.locateCenterOnScreen("play.png", grayscale=False, confidence=0.5)
            log("play: ", "a")
            log(play, "a")
            if play is not None:
                pyautogui.click(play)
                time.sleep(3)
                accept = pyautogui.locateCenterOnScreen("accept.png", grayscale=False, confidence=0.5)
                log("accept: ", "a")
                log(accept, "a")
                if accept is not None:
                    pyautogui.click(accept)
                    time.sleep(int(tempo))
                    close = pyautogui.locateCenterOnScreen("close.png", grayscale=False, confidence=0.5)
                    log("close: ", "a")
                    log(close, "a")
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
                                log(close, "a")
                                print("Please report this bug/error on github")
                                break
                    else:
                        log("close is None", "a")
                        print("Please report this bug/error on github")
                        break
                else:
                    log("accept is None", "a")
                    print("Please report this bug/error on github")
                    break
            else:
                log("play is None", "a")
                print("Please report this bug/error on github")
                break
    else:
        log("problem with prove.png. return = ", "a")
        log(provebutton, "a")
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
    d1 = datetime.now()
    log(d1, "w+")
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
    main()
