from Tools import *


def GradientDescent(f, start, e, l):
    point = start.copy()
    stop = False
    grad = Gradient(f, point)
    while not stop:
        if GradientLenghtSq(grad) > e ** dec(2):
            point = point - l*grad
            grad = Gradient(f, point)
        else:
            break
    print(point[0])
    print(point[1])
    return f(point)