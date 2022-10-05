from params import *
from calculateModel import *
import route as r
import math

def main():
    test = inputs() 
    #calculateModel(test.speed,test.alt)

    #timeToFinish = r.distance / r.speedLimit
    #print(timeToFinish, 'h')
    
    Cd = 0.1
    ACd = 0.2
    wWeight = 3790
    speed = 90
    EPKa = (0.0125)(speed^2)(0.2)
    EPKr = rr*(1+(speed/161))*wWeight
    print(EPK)

    exit(0)

main()
