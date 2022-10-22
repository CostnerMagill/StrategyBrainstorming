from params import *
from route import *

def calculateModel():
    air_density = (-3.64*(10**-14))*(elevation)**3+(3.88*(10**-9))*(elevation)**2-(1.18*(10**-4))*(elevation)+1.17
    
    #Aero Drag Power Model
    aero_power = 0.5 * air_density * (speed_ms**3) * drag_area #Drag power in watts
    #speed_ms^ is velocity atm. will need to add for headwind/tailwind (+head/-tail)

    #Rolling Resistance Model
    rolling_resistance_power =  0.278 * rolling_resistance * (1+target_speed/161) * (weight) * target_speed #0.278 is a unit conversion and speed is in kph. gives rr power loss in watts

    #Array Power Model
    #average array power is imported with params

    total_power = avg_array_power - aero_power - rolling_resistance_power
    energy_per_hour = abs(total_power)
    max_time = battery_energy/energy_per_hour
    max_dist = target_speed*max_time
    
    print(max_time, max_dist)

    #Motor Model
    #dR = (Crr)*(1+(speed/161))*weight    #Rolling Resistance

    #motorVoltage = speed / radius * kBEMF/3 + Irms * phaseResistance
    #motorPower = 3 * motorVoltage * Irms
