##P4.34

A = float(input('Please enter A (rate prey birth exceed natural death): '))
B = float(input('Please enter B (rate of predation): '))
C = float(input('Please enter C (rate predator death exceed birth without food): '))
D = float(input('Please enter D (predator incerease in presence of food): '))

PRED_INI = int(input('Please enter initial population of predator: '))
PREY_INI = int(input('Please enter initial population of prey: '))

period = int(input('Please enter the period: '))

#A = 0.1
#B = 0.01
#C = 0.01
#D = 0.00002

#PRED_INI = 20
#PREY_INI = 1000

#pred = PRED_INI
#prey = PREY_INI

pred_old = pred
prey_old = prey

#period  = 1020

for i in range(period):
    prey = prey * (1+A - B*pred_old)
    pred = pred * (1-C + D*prey_old)

    prey_old = prey
    pred_old = pred

print('After %d, there are %d prey and %d predator left.' %(period, prey, pred))

