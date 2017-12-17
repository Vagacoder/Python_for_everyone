## Ch05 P 5.32
from math import *

def Watch_Angle(angle, screen_bottom, screen_height):
    A = radians(angle)
    SCREEN_BOTTOM = screen_bottom
    SCREEN_HEIGHT = screen_height

    distance = float(input('Please enter the distance from screen: '))

    h = distance * tan(A)
    alpha = degrees(atan((SCREEN_BOTTOM - h)/distance))
    beta = degrees(atan((SCREEN_HEIGHT + SCREEN_BOTTOM - h)/distance))

    theta = beta - alpha

    return theta

print(Watch_Angle(8, 6, 24))

## Ch05 P 5.33

def focus_lens(n, R1, R2, d):
    focus_inverse = (n-1)*((1/R1)-(1/R2)+((n-1)*d)/(n*R1*R2))
    return 1/focus_inverse

## Ch05 P 5.34
from math import *

def volume_barrel(h, R1, R2):
    vol = 1/3 * pi * h *(R1**2 + R2 **2 + R1 * R2)
    return vol

def surface_barrel(h, R1, R2):
    surface = pi *(R1+R2)*sqrt((R2-R1)**2 + h**2 ) + pi * R1**2
    return surface
