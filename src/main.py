from random import randint
from time import sleep
from turtle import delay
from params import *
from route import *
from calculateModel import *
import route as r
from math import *
from tkinter import *
from tkinter import ttk
def main():
    '''
    test = inputs() 
    #calculateModel(test.speed,test.alt)
    #timeToFinish = r.distance / r.speedLimit
    #print(timeToFinish, 'h')
    Cd = 0.1
    ACd = 0.2
    wWeight = 3790
    speed = 90
    EPKa = (0.0125)*(speed**2)*(0.2)
    EPKr = rr*(1+(speed/161))*wWeight
    print(calculateModel(speed,test.alt))
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Startigizer").grid(column=0,row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1,row=0)
    root.mainloop()
    '''
    while(True):
        output = randint(0,100)/randint(0,100)
        calculateModel(targetSpeed,elevation)
        print(output)
        sleep(2)


main()
