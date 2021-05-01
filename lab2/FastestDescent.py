import numpy
from Tools import *

def FastestDescent(f, start, e):
    point = start.copy()
    grad = Gradient(f, point)
    while True:
        if GradientLenghtSq(grad) < e ** dec(2):
            break
        #l = (GoldenRatio(lambda alpha: f(point - alpha * grad), e))
        l = (Fibonacci(lambda alpha: f(point - alpha * grad), e))
        point = point - l*grad
        grad = Gradient(f, point)

    print(point[0])
    print(point[1])
    return f(point)