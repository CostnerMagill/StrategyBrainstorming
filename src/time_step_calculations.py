from params import *
from route import *
from sympy.solvers import solve
from sympy import symbols

t_step = 5 # Seconds
weight = 3790 # Newtons 

def main():
    velocity = 100 # Kilometers per hour
    while (velocity > 0):
        pack_energy = 4500 # Watt Hours
        current_velocity = velocity # in kph

        while(pack_energy > 0):
            delta_KE = 0
            delta_KE += aero()
            #delta_KE += rolling_resistance()
            pack_energy += array()
            pack_energy += motor(delta_KE)
            #pack_energy += parasitic()
        velocity -= 1

def aero():
    air_density = (-3.64*(10**-14))*(elevation)**3+(3.88*(10**-9))*(elevation)**2-(1.18*(10**-4))*(elevation)+1.17 #air density in kg/m^3
    aero_power = 0.5 * air_density * ((current_velociy*(1/3.6))**3) * drag_area #Drag power in watts
    k_energy = (aero_power * t_step)/3600 #calculates watt-seconds and converts to watt-hours
    return k_energy

def array(pack_energy):
    return (700 * t_step / 3600) 

# def parasitic():
#     return (average_parasitic_power * t_step)

def rolling_resistance(current_velocity):
    rr_coefficient = 0.0055 
    rr_power = rr_coefficient * weight * (1 + (current_velocity/161)) # Watt hours
    return rr_power

def motor(delta_KE):
    return (-delta_KE)

main() 