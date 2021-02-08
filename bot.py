import pyautogui
import time
from datetime import datetime


def log(message,modo):
    f = open("log.txt",modo)
    f.write(str(message))
    f.write("\n")
    f.close


def Raid(run):
    log("raid","a")
    time.sleep(1)
    if(run<1):
        log("run<1","a")
        pyautogui.alert(text='the number of raid runs must be 1 or greater',button='OK')
        exit
    else:
        raidcord = pyautogui.locateCenterOnScreen("test1.png",grayscale=False,confidence=0.4)
        log("run: ","a")
        log(run,"a")
        log(raidcord,"a")
        if raidcord!=None:
            pyautogui.click(raidcord)
            time.sleep(1)
            evoca = pyautogui.locateCenterOnScreen("startraid.png",grayscale=False,confidence=0.5)
            log("evoca: ","a")
            log(evoca,"a")
            if(evoca!=None):
                pyautogui.click(evoca)
                time.sleep(1)
                #if(difficult=='heroic'):
                difficult = pyautogui.locateCenterOnScreen("eroic.png",grayscale=False,confidence=0.5)
                log("difficult: ","a")
                log(difficult,"a")
                if(difficult!=None):
                    pyautogui.click(difficult)
                    time.sleep(1)
                    accept = pyautogui.locateCenterOnScreen("accept.png",grayscale=False,confidence=0.5)
                    log("accept: ","a")
                    log(accept,"a")
                    if(accept!=None):
                        pyautogui.click(accept)
                        #tempo dedicato al completamento del raid in auto
                        time.sleep(240)
                        while True:
                            if(run==1):
                                yes = pyautogui.locateCenterOnScreen("yes.png",grayscale=False,confidence=0.5)
                                log("yes: ","a")
                                log(yes,"a")
                                time.sleep(1)
                                pyautogui.click(yes)
                                break
                            else:
                                run=run-1
                                rerun = pyautogui.locateCenterOnScreen("rerun.png",grayscale=False,confidence=0.5)
                                log("rerun: ","a")
                                log(rerun,"a")
                                time.sleep(1)
                                pyautogui.click(rerun)
                                time.sleep(260)
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

print("Start")
    

 
if __name__ == '__main__':
    main()
