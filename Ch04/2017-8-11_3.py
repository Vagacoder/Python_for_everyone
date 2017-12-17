## P4.35

DELTA_T = 0.01
G = 9.81

INI_V = float(input('please enter the initial velocity (m/s): '))
#INI_V = 100

s = 0
v = INI_V

for i in range(2500):
    s = s + v * DELTA_T
    v = v - G * DELTA_T
    if i%100 == 0:
        print('At time of %3d sec: s is %.2f m, v is %.2f m/s.'%(i/100, s, v))
        print('Theoratic s = %.2f m. \n' %((-1/2) * G * (i/100)**2 + INI_V * (i/100)))

## P4.36

B = float(input('please enter B: '))
L = float(input('please enter L: '))
T = float(input('please enter T: '))
x = float(input('please enter x: '))
n = int(input('please enter n (integer only): '))

#B = 10
#L = 20
#T = 10
#x = 1
#n = 4

Y_INI = B/2*(1-(2*x/L)**2)*(1-(0/T)**2)

y = Y_INI
area_total = 0

for i in range(1,n+1):
#    print('i is', i)
    z = -i*T/n
#    print('z is', z)
    y_pre = y
#    print('y_pre is', y_pre)
    y = B/2*(1-(2*x/L)**2)*(1-(z/T)**2)
#    print('y is', y)
    area = (y_pre + y)*T/n/2
#    print('area is', area)
    area_total += area

print(area_total)

## P4.37
from math import *

h = 6

A_INI = 1
a = A_INI

for i in range(1,25):
    a_pre = a
    a = A_INI * exp(i *log(1/2)/h)
    print(a)
    print('At hour %2d, A/A0 = %.5f.' %(i, a/A_INI))

## P4.38

R0 = 20
Rs = 8
Vs = 40

n_INI = 0
n = n_INI

for i in range(1, 201):
    n += i * 0.01
    Ps = Rs* (n*Vs /(n**2*R0 + Rs))**2
    print('Current n is %7.2f and Ps is %8.4f' %(n, Ps))


