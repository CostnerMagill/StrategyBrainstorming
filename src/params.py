
#currently g6 params

#Aero/Mechanical params
dA =  2*29.33/ 1.21/18^2; #From Ansys, which uses 1.21 as the air density
rR =  .0047 #Rolling resistance
mass = 730/2.2

#Motor Params
phaseResistance = 0.034
max_I = 70
kBEMF = 1.17
kTau = 1.17
radius = 11/39

#Battery Params
DC_Voltage = 126 #V
DC_Imax = 150 #A
DC_Imin = -60 #A
idlePower = 22 #W