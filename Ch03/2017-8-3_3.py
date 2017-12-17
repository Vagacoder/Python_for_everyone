## Ch03 3.26
from sys import *

volume_unit = 'fl oz gal ml l'
weight_unit = 'lb g kg'
length_unit = 'in ft mi mm cm m km'

input_unit = input('Enter the unit you want to convert from: ').lower()
output_unit = input('Enter the unit you want to convert to: ').lower()

if (input_unit in volume_unit) and (output_unit in volume_unit):
    mode = 'V'

elif (input_unit in weight_unit) and (output_unit in weight_unit):
    mode = 'W'

elif (input_unit in length_unit) and (output_unit in length_unit):
    mode = 'L'

else:
    exit('Incompatible input units, please try again.')

value = float(input('Enter the value to convert: '))

if mode == 'V':
    fl_2_oz = 0.125
    fl_2_gal = 0.0009766
    fl_2_ml = 3.6966912
    fl_2_l = 0.0036967

    oz_2_fl = 1 / fl_2_oz
    oz_2_gal = 0.0078125
    oz_2_ml = 29.5735296
    oz_2_l = 0.0295735

    gal_2_fl = 1 / fl_2_gal
    gal_2_oz = 1 / oz_2_gal
    gal_2_ml = 3785.411784
    gal_2_l = 3.7854118

    ml_2_fl = 1 / fl_2_ml
    ml_2_oz = 1 / oz_2_ml
    ml_2_gal = 1 / gal_2_ml
    ml_2_l = 0.001

elif mode == 'W':
    lb_2_g = 453.59237
    lb_2_kg = 0.4535924

    g_2_lb = 1/lb_2_g
    g_2_kg = 0.001

    kg_2_lb = 1/lb_2_kg
    kg_2_g = 1000

elif mode == 'L':
    in_2_ft = 0.0833333
    in_2_mi = 0.0000158
    in_2_mm = 25.4
    in_2_cm = 2.54
    in_2_m = 0.02540
    in_2_km = 0.0000254

    ft_2_in = 12
    ft_2_mi = 0.0001894
    ft_2_mm = 304.8
    ft_2_cm = 3.048
    ft_2_m = 0.3048
    ft_2_km = 0.0003048

    mi_2_in = 63360
    mi_2_ft = 5280
    mi_2_mm = 1609344
    mi_2_cm = 160934.4
    mi_2_km = 1.609344

## skip mm cm m km exchange rate


#print('exchange = ' + input_unit + '_2_' + output_unit)
exec('exchange =' + input_unit + '_2_' + output_unit)
#print(exchange)
#print(type(exchange))

print('%.2f %s = %.2f %s' %(value, input_unit, exchange * value, output_unit))