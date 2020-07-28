import numpy as np
import math

def getDigit(n,k):
    return (n // (10**k)) % 10

assert(getDigit(123,0) == 3)
assert(getDigit(123,1) == 2)
assert(getDigit(123,2) == 1)
assert(getDigit(123,3) == 0)
assert(getDigit(123,8) == 0)

def colorBlender(rgb1, rgb2, midpoints, n):
    level = n/(midpoints+1)

    blend = rgb1

    for i in range(len(rgb1)):
        if ( (1-level) * rgb1[i] + level*rgb2[i] ) % 0.5 == 0.0:
            blend[i] = math.ceil((1-level) * rgb1[i] + level*rgb2[i])
        else:
            blend[i] = (1-level) * rgb1[i] + level*rgb2[i]
    return blend

c1 = np.array([220, 20, 60])
c2 = np.array([189, 252, 201])

assert(colorBlender(c1,c2,3,0).all() == c1.all() )
assert(colorBlender(c1,c2,3,0).all() == np.array([212, 78, 95]).all() )
assert(colorBlender(c1,c2,3,0).all() == np.array([205, 136, 131]).all() )
assert(colorBlender(c1,c2,3,0).all() == np.array([197, 194, 166]).all() )
assert(colorBlender(c1,c2,3,0).all() == c2.all() )

print(colorBlender(c1, c2, 10,2))
