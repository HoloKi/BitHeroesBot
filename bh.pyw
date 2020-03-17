from PIL import Image, ImageGrab
import os
import time

#assumo che il gioco sia alla risoluzione base di quando si inizia da 0 
#metterlo in altro a sinistra in modo che l'angolo del gioco combaci con l'angolo dello schermo 
#global dichiaration
x_pad = -1
y_pad = -1
 
def screenGrab():
    box = (x_pad+1,y_pad+1,x_pad+795,y_pad+598)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')
 
def main():
    screenGrab()
 
if __name__ == '__main__':
    main()