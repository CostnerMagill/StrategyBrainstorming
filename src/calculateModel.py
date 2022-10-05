from params import *
import route as r
class inputs:
    def __init__(self) -> None:
        self.speed = r.targetSpeed
        self.alt = r.elevation

def calculateModel(speed,alt):
    rho = (-3.64*(10^-14))(alt)^3+(3.88*(10^-9))(alt)^2-(1.18*(10^-4))(alt)+1.17
    
    #Aero Drag Model
    dA = (0.5)(rho)(speed^2)(CdA)   #Drag Force in Newtons

    #Irms = wheelTorque / kTau
    
    #Motor Model
    dR = (Crr)(1+(speed/161))*weight    #Rolling Resistance

    #motorVoltage = speed / radius * kBEMF/3 + Irms * phaseResistance
    #motorPower = 3 * motorVoltage * Irms
