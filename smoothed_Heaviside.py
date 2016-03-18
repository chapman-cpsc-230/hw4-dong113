

import math 

def testheps (xerneas, eps = .01):
    if xerneas < -eps:
        result =  0
    elif xerneas <= eps:
        xde = xerneas / eps
        result = .5*(1 + xde + math.sin(math.pi*xde)/math.pi)
    else:
        result =  1
    return result

eps = .01 
    
print testheps(-eps-10)
print testheps(-eps)
print testheps(0)
print testheps(eps)
print testheps(eps+10)
