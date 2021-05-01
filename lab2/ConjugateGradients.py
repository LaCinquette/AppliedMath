from Tools import *

def D(derivative):
    i = 0
    s = dec(0)
    while i < len(derivative):
        derivative[i] = derivative[i]**2
        i += 1
    return derivative


def ConjugateGradients(f, start, e):
    pre_point = start.copy()
    pre_p = - Gradient(f, pre_point)
    a = GoldenRatio(lambda alpha: f(pre_point + alpha * pre_p), e)

    point = pre_point + a * pre_p
    b = dec(GradientLenghtSq(Gradient(f, point)) / dec(GradientLenghtSq(Gradient(f, pre_point))))
    p = - Gradient(f, point) + pre_p * b
    while GradientLenghtSq(Gradient(f, point)) > e ** dec(2):
        pre_point = point
        pre_p = p
        a = GoldenRatio(lambda alpha: f(pre_point + alpha * pre_p), e)
        point = pre_point + a * pre_p
        b = dec(GradientLenghtSq(Gradient(f, point)) / dec(GradientLenghtSq(Gradient(f, pre_point))))
        p = - Gradient(f, point) + pre_p * b
    print(point[0])
    print(point[1])
    return f(point)

def ConjugateGradientsS(f, start, e, l):
    n = len(start)
    x = [start.copy()] * n
    p = [- Gradient(f, x[0])] * n
    b = [dec(0)] * n
    a = [dec(0)] * n
    i = 1
    x[i] = x[i-1] + a[i-1] * p[i-1]
    #while i < n:
    return x[10]