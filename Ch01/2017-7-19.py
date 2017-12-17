from math import *

TILE_WIDTH = 5
TOTAL_WIDTH = 100
number_pairs = (TOTAL_WIDTH - TILE_WIDTH)//(TILE_WIDTH*4)
number_tiles = 1 + 4*number_pairs
gap_size = (TOTAL_WIDTH - (number_tiles*TILE_WIDTH))/2.0
print('The number of tiles are',number_tiles)
print('The gap size is',gap_size)

M_COST_1Y = 100
M_COST_10Y = 1500
inc_M_Cost = (M_COST_10Y - M_COST_1Y)//9
m_Cost_3y = 100 + inc_M_Cost*(3-1)
print('The maintance cost at year 3 is about', m_Cost_3y)

r1 = 3.6
r2 = 1.2

h1 = 15
h2 = 7
h3 = 6


v1 = pi * r1**2 * h1
v2 = pi * r2**2 * h2
v3 =(pi * (r1**2 + r1*r2 + r2**2) * h3)/3

v = v1 + v2 + v3

print(v1)
print(v2)
print(v3)
print('The volumn of bottle is', v, 'cm3.')
