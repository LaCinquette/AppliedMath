import random as rnd
import numpy as np
from Tools import dec

def FunctionGenerator(n, k):
    k = k / n
    res = ' '
    for i in range(n):
        res += '(a[' + str(i) + ']**dec('+ str(k) +'))'
        if i != n - 1:
            res += ' + '
    return res

print(FunctionGenerator(4, 4))
print(FunctionGenerator(4, 5))
print(FunctionGenerator(4, 6))
print(FunctionGenerator(4, 7))
print(FunctionGenerator(4, 8))