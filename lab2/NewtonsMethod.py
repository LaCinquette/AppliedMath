from Tools import *


def NewtonMethod(f, start, e):
    point = start.copy()
    while GradientLenghtSq(Gradient(f, point)) > e ** dec(2):
        point = point - Multiplication(reverseH(), Gradient(f, point))
    print(point[0])
    print(point[1])
    return f(point)