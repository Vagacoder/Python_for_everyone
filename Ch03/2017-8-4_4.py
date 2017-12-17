## Ch 03 P3.41

#vm = float(input('receive Vm: '))
vm =13.4

if vm <12 or vm > 18:
    exit('error, Vm is out of range.')

RS = 75
k = 0.5
R0 = 100
Vs = 20

temp = RS/k * vm/(Vs-vm) - R0/k

print('The temperature is %.2f C.' % temp)

## Ch 03 P3.42
from math import *

#temp_F = float(input('Please enter F degree: '))
temp_F = 15

temp_C = (temp_F - 32)*5/9
T = temp_C +273

R0 = 33192
R2 = 156300
R3 = R2
R4 = R2

T0 = 40 + 273
b = 3310

R = R0 * exp(b*(1/T - 1/T0))

if R2/(R+R2) < R4/(R3+R4):
    print('Alarm! '*3)

else:
    print('Good temp!')

## Ch03 P3.44

speed1 = 1
speed2 = 10
speed3 = 20
speed4 = 40

r = 3
Tmax = 60

#m = float(input('Please enter the mass(in kg): '))
m = 0.1

T1 = m*speed1**2/r
#print(T1)
T2 = m*speed2**2/r
#print(T2)
T3 = m*speed3**2/r
#print(T3)
T4 = m*speed4**2/r
#print(T4)

if T4 <= Tmax:
    print('40 m/s is a good speed.')
elif T3 <= Tmax:
    print('20 m/s is a good speed.')
elif T2 <= Tmax:
    print('10 m/s is a good speed.')
elif T1 <= Tmax:
    print('1 m/s is a good speed.')
else:
    print('Too heavy. no speed is safe.')

## Ch03 P3.45

G = 6.67E-11
Mass = 2.2E14
R = 9400

v_escape = sqrt(2 * G * Mass /R)
print('Escaping', v_escape)

v_lauch1 = float(input('Please enter launch velocity(in mph): '))
v_lauch = v_lauch1 * 0.44704

if v_lauch < v_escape:
    print('Return!')
else:
    Mass1 = R*v_lauch**2 /(2 * G)
    print('Mass must be or larger than %.2f kg.' %Mass1)
