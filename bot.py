from PIL import Image, ImageGrab, ImageOps
import os
import time
import win32api,win32con
from numpy import *

#assumo che il gioco sia alla risoluzione base di quando si inizia da 0 
#metterlo in altro a sinistra in modo che l'angolo del gioco combaci con l'angolo dello schermo 
#global dichiaration
x_pad = -1
y_pad = -1
 
def screenGrab():
    box = (x_pad+1,y_pad+1,x_pad+795,y_pad+598)
    im = ImageGrab.grab(box)
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +'.png', 'PNG')
    return im

def grab():
    box = (x_pad+1,y_pad+1,x_pad+795,y_pad+598)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    return a

def get_endraid():
    box = (243,262,545,366)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    #im.save(os.getcwd() + '\\endraid_one__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def main():
    pass
 
if __name__ == '__main__':
    main()

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print ("Click.")

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print ("left Down")
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print ("left release")

def mousePos(cord): 
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print (x,y)

class Cord:

    f_raid = (39,351)
    f_raidshard = (362, 119)
    f_finishraid = ()
    
class Blank:
    bubble_1 = 2343
    
def Raid():
    s = screenGrab()
    time.sleep(.1)
    while (s.getpixel(Cord.f_raidshard) != (179, 61, 150)):
        s1 = get_endraid()
        while(s1 != Blank.bubble_1 ):
            #location del raid
            mousePos((39,351))
            leftClick()
            time.sleep(2)
         
            #location di Evoca
            mousePos((533,425))
            leftClick()
            time.sleep(2)
             
            #location di Eroico
            mousePos((584,293))
            leftClick()
            time.sleep(2)
             
            #location per accettare il team
            mousePos((511,518))
            leftClick()
            time.sleep(1)

            #accertamento che non ci siano shard
            s = screenGrab()
            while True:
                s1 = get_endraid()
                time.sleep(60)
                y = s1
                s2 = get_endraid()
                if (s2 == y):
                    break;
            #location per terminare
            mousePos((340, 426))
            leftClick()
            time.sleep(1)
