## CH1 P2.1
## This program is calculating the dimesions (in mm) of letter size (8x11 inch) paper

#25.4 millimeter = 1 inch
MM_PER_INCH = 25.4

#the size of letter size paper (in inch)
widthINCH = 11
heightINCH = 8

print('The width of letter size paper is', widthINCH*MM_PER_INCH, 'mm.')
print('The height of letter size paper is', heightINCH*MM_PER_INCH, 'mm.')

#=================
# CH1 P2.2
# This program is calculating the perimeter and diagonal of letter size paper
import math

MM_PER_INCH = 25.4

widthINCH = 11
heightINCH = 8

perimeter = (widthINCH*2 + heightINCH*8)*MM_PER_INCH
diagonal = (math.sqrt(widthINCH*widthINCH + heightINCH*heightINCH))*MM_PER_INCH

print ('The perimeter of letter size paper is', perimeter, 'mm.')
print ('The diagonal of letter size paper is', diagonal, 'mm.')


