from params import *
from route import *
from sympy.solvers import solve
from sympy import symbols

t_step = 5 # seconds
velocity = 65

while (velocity > 0):
    pack_energy = 4500
    current_velocity = velocity

    while(pack_energy > 0):
        delta_v = 0
        #aero(KE)
        #array(SOC)
        #parasite(SOC)
        #rolling_resistance(KE)
        #motor(SOC, KE)
    velocity -= 1

def aero(k_energy):
    pass

def array(pack_energy):
    pass

def parasite(pack_energy):
    pass

def rolling_resistance(k_energy):
    pass

def motor(pack_energy, k_energy):
    pass