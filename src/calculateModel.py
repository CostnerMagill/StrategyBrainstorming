from params import *
from route import *
from sympy.solvers import solve
from sympy import symbols

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

    v = symbols("V")
    target_average_speed_list = solve(battery_energy + (avg_array_power*distance)/v - 0.0025*(v**2)*distance - 0.278*rolling_resistance*weight*distance*(1+(v/161))) #need to parse result and find answer
    
    target_average_speed = 0
    for i in range(len(target_average_speed_list)):
        if target_average_speed_list[i].is_real:
            if target_average_speed_list[i] > target_average_speed:
                target_average_speed = target_average_speed_list[i]
    
    print (target_average_speed)
    
    
    #Motor Model
    #dR = (Crr)*(1+(speed/161))*weight    #Rolling Resistance

    #motorVoltage = speed / radius * kBEMF/3 + Irms * phaseResistance
    #motorPower = 3 * motorVoltage * Irms
