from params import *

#Energy

def calculateModel(speed):
    
    #Aero Drag Model
    
    
    Irms = wheelTorque / kTau
    
    #Motor Model
    motorVoltage = speed / radius * kBEMF/3 + Irms * phaseResistance
    motorPower = 3 * motorVoltage * Irms
    
    
    exit(0)
