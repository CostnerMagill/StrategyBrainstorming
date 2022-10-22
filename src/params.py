#Aero/Mechanical params

mass = 730/2.2 #in kg
weight = 3790 #in newtons
rolling_resistance = .0055
drag_area = 0.2 #From Ansys, which uses 1.21 as the air density, Maybe account for rho later

#Motor Params
phase_resistance = 0.034
max_I = 70
kBEMF = 1.17
kTau = 1.17
radius = 11/39

#Battery Params
DC_Voltage = 126 #V
DC_Imax = 150 #A
DC_Imin = -60 #A
idle_power = 22 #W
battery_energy = 4000 #battery energy in watt hours
avg_array_power = 700 #watts
