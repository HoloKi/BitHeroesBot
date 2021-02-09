import pyautogui
import time
from datetime import datetime


def log(message,modo):
    f = open("log.txt",modo)
    f.write(str(message))
    f.write("\n")
    f.close

hero = "heroic"
hard = "hard"
norm = "normal"

def menu():
    print("Digita il numero per selezionare l'opzione desiderato")
    print("1)Per utilizzare la funzione Raid\n")
    a = input("Seleziona numero: \n")
    if int(a)==1:
        b = input("Digita il numero di run: \n")
        c = input("Digita 1)normal 2)hard 3)heroic in base alla difficoltà che desideri\n")
        d = input("Digita il numero relativo a quanto impieghi a completare una run del raid in secondi.\n Attento, non essere preciso, meglio avere del tempo in piu per eventuali\n")
        if int(c)==1:
            Raid(b,norm,d)
        else:
            if int(c)==2:
                Raid(b,hard,d)
            else:
                if int(c)==3:
                    Raid(b,hero,d)
                else:
                    print("Qualcosa è andato storto con la digitazione dei numeri")
    else:
        print("Non ci sono altre opzioni")

def Raid(run,difficult,duration):
    #run = numero di shard
    #difficult = difficoltà
    #duration = quanto dura in secondi una run
    log(f"{difficult},{duration}","a")
    log("raid","a")
    time.sleep(1)
    if(int(run)<1):
        log("run<1","a")
        pyautogui.alert(text='the number of raid runs must be 1 or greater',button='OK')
        exit()
    else:
        raidcord = pyautogui.locateCenterOnScreen("test1.png",grayscale=False,confidence=0.5)
        log("run: ","a")
        log(run,"a")
        log(raidcord,"a")
        if raidcord!=None:
            pyautogui.click(raidcord)
            time.sleep(1)
            evoca = pyautogui.locateCenterOnScreen("startraid.png",grayscale=False,confidence=0.5)
            log("evoca: ","a")
            log(evoca,"a")
            if evoca!=None:
                pyautogui.click(evoca)
                time.sleep(1)
                if difficult==hero:
                    difficulty = pyautogui.locateCenterOnScreen("eroic.png",grayscale=False,confidence=0.4)
                    print(difficulty)
                if difficult==hard:
                    difficulty = pyautogui.locateCenterOnScreen("hard.png",grayscale=False,confidence=0.5)
                    print(difficulty)
                if difficult==norm :
                    difficulty = pyautogui.locateCenterOnScreen("normal.png",grayscale=False,confidence=0.5)
                    print(difficulty)
                if(difficult!=norm and difficult!=hard and difficult!=hero):
                    print("oh no")
                    exit()
                log("difficulty: ","a")
                log(difficulty,"a")
                if difficulty!=None:
                    pyautogui.click(difficulty)
                    time.sleep(1)
                    accept = pyautogui.locateCenterOnScreen("accept.png",grayscale=False,confidence=0.5)
                    log("accept: ","a")
                    log(accept,"a")
                    if accept!=None:
                        pyautogui.click(accept)
                        #tempo dedicato al completamento del raid in auto
                        time.sleep(int(duration))
                        while True:
                            if int(run)==1:
                                print(f"run debug = {run}")
                                yes = pyautogui.locateCenterOnScreen("yes.png",grayscale=False,confidence=0.5)
                                log("yes: ","a")
                                log(yes,"a")
                                time.sleep(1)
                                pyautogui.click(yes)
                                time.sleep(1)
                                xbutton = pyautogui.locateCenterOnScreen("xbutton.png",grayscale=False,confidence=0.5)
                                pyautogui.click(xbutton)
                                break
                            else:
                                print(f"run debug = {run}")
                                run=int(run)-1
                                rerun = pyautogui.locateCenterOnScreen("rerun.png",grayscale=False,confidence=0.5)
                                log("rerun: ","a")
                                log(rerun,"a")
                                time.sleep(1)
                                pyautogui.click(rerun)
                                time.sleep(int(duration))
                    else:
                        print("AcceptError")
                        exit
                else:
                    print("DifficultError")
                    exit
            else:
                print("EvocaError")
                exit
        else:
            print("RaidError")
            exit

def main():
    d1 = datetime.now()
    log(d1,"w+")
    #a = input("inserisci il numero di run del raid: \n")
    #b = input("inserisci il la difficoltà del raid scrivendo norm = normal, hard = hard o hero = heroic\n ")
    #print(b)
    #c = input("Inserisci il tempo impiegato per finire una run(in secondi). Attento...meglio dare qualche secondo in piu! \n")
    #Raid(a,str(b),c)
    menu()

print("Start")
    

 
if __name__ == '__main__':
    main()
