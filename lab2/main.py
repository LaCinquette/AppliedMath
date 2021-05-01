from array import *

from ConjugateDirections import ConjugateDirectionsOfPowell
from ConjugateGradients import *
from FastestDescent import *
from GradientDescent import *
from Tools import *
import numpy
from NewtonsMethod import *

f = lambda a: (a[0]**2)/15 + a[1]**2 + a[1]
f2 = lambda a: (a[0]**2)/15 + a[0] + 1
start = numpy.array([dec(4), dec(1)])
e = dec(0.01)
l = dec(0.001)
#print(Gradient(f, start))
print(GradientDescent(f, start, e, l))
print("aaa")
print(ConjugateGradients(f, start, e))
print("aaa")
print(NewtonMethod(f, start, e))
rev = ([dec(5), dec(6), dec(2)], [dec(7), dec(4), dec(5)], [dec(1), dec(3), dec(2)])
grad = ([dec(1), dec(2), dec(3)])
#print(Multiplication(rev, grad))


