
from audioop import avg
from logging.handlers import TimedRotatingFileHandler
from math import floor


avg_array_power = 700 #watts
battery_energy =  4500 #watt hours
weight = 3790 #newtons
rolling_resistance = 0.0055
drag_area = 0.2 #m^2 #this is the result of A * Cd
speed = 90 #kph
speed_ms = 1/3.6 * speed #speed in meter
air_density = 1.17

def main():
    
    aero_power = 0.5 * air_density * (speed_ms**3) * drag_area
    aero_power = floor(aero_power)
    rolling_resistance_power = 0.278 * rolling_resistance * (1+ speed/161) * weight * speed
    rolling_resistance_power = floor(rolling_resistance_power)
    total_power =  avg_array_power - aero_power - rolling_resistance_power
    energy_per_hour = abs(total_power) #variable name for clarification
    time = battery_energy / energy_per_hour
    print(total_power,time, rolling_resistance_power, aero_power)


main()