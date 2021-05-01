import numpy

from Tools import *


def ConjugateDirectionsOfPowell(f, start, e):
    x = start.copy()
    h1 = numpy.array([dec(0)] * len(start))
    h2 = numpy.array([dec(0)] * len(start))
    h1[0] = dec(1)
    h2[len(start) - 1] = dec(1)
    if GradientLenghtSq(Gradient(f, x)) < e ** dec(2):
        return f(x)
    while True:
        h = Golden(lambda alpha: f(x + alpha * h2), e)
        x1 = x + h * h2
        if GradientLenghtSq(Gradient(f, x1)) < e ** dec(2):
            return f(x1)
        h = Golden(lambda alpha: f(x1 + alpha * h1), e)
        x2 = x1 + h * h1
        if GradientLenghtSq(Gradient(f, x2)) < e ** dec(2):
            return f(x2)
        x = x2

def Golden(func, e):
    c = dec(0.6180339887498949)
    Left = -1
    Right = 1
    x1 = Left + (1 - c) * (Right - Left)
    x2 = Left + c * (Right - Left)
    f1 = func(x1)
    f2 = func(x2)
    delta = (Right - Left)
    while delta/2 > e:
        if f1 < f2:
            Right = x2
            x2 = x1
            f2 = f1
            x1 = Left + (Right - Left) * (1 - c)
            f1 = func(x1)
        else:
            Left = x1
            x1 = x2
            f1 = f2
            x2 = Left + (Right - Left) * c
            f2 = func(x2)
        delta = (Right - Left)
    return (Left + Right) / dec(2)