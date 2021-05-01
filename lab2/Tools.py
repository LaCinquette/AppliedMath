import cmath
import decimal
import math

def dec(x):
    return decimal.Decimal(x)

d = dec(0.00000001)

def Derivative1(f, point, i):
    _point = point.copy()
    _point[i] += d
    return (f(_point) - f(point))/d

def Derivative2(f, point, i):
    _point = point.copy()
    sum = - 2 * f(_point);
    _point[i] += d
    sum += f(_point)
    _point[i] -= 2*d
    sum += f(_point)
    return (sum)/d**dec(2)

def Gradient(f, point):
    grad = point.copy()
    i = 0
    while i < len(point):
        grad[i] = Derivative1(f, point, i)
        i += 1
    return grad

def GradientLenghtSq(gradient):
    sum = dec(0)
    i = 0
    while i < len(gradient):
        sum += gradient[i]**dec(2)
        i +=1
    return sum

def Distance2(point1, point2):
    sum = dec(0)
    i = 0
    while i < len(point1):
        sum += (point2[i] - point1[i])**dec(2)
        i +=1
    return sum

def H():
    Hex1 = [[dec(2/15), dec(0)], [dec(0), dec(2)]]
    return Hex1

def reverseH():
    Hex = H()
    revers = Hex
    d = DetH()
    revers[0][0] = Hex[1][1]/d
    revers[1][1] = Hex[0][0]/d
    revers[0][1] = - Hex[1][0]/d
    revers[1][0] = - Hex[0][1]/d
    revers = [[dec(2 / 0.267), dec(0)], [dec(0), dec(0.5)]]
    return revers

def Multiplication(Hex, grad):
    n = len(grad)
    i = 0
    Mul = [dec(0)] * n
    while i < n:
        j = 0
        while j < n:
            Mul[i] += Hex[i][j] * grad[j]
            j += 1
        i += 1
    return Mul

def Dot(v1, v2):
    i = 0
    dot = dec(0)
    while i < len(v1):
        dot += dec(v1[i] * v2[i])
        i += 1
    return dot

def DetH():
    Hex = H()
    return Hex[0][0] * Hex[1][1] - Hex[1][0] * Hex[0][1]

def FibonacciSequence(n):
    x1 = (1 + cmath.sqrt(5))/2
    x2 = (1 - cmath.sqrt(5))/2
    x1 = x1**n
    x2 = x2**n
    if round(((x1 - x2)/cmath.sqrt(5)).real) == 0:
        return 1
    return round(((x1 - x2)/cmath.sqrt(5)).real)

def NSearch(distant, e):
    i = 1
    while FibonacciSequence(i + 2) <= distant / e:
        i += 1
    return round(i)

def GoldenRatio(func, e):
    c = dec(0.6180339887498949)
    Left = 0
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

def Fibonacci(func, e):
    Left = dec(0)
    Right = dec(1)
    c = NSearch((Right - Left), e)
    x1 = Left + dec(FibonacciSequence(c) / FibonacciSequence(c + 2)) * dec(Right - Left)
    x2 = Left + dec(FibonacciSequence(c + 1) / FibonacciSequence(c + 2)) * dec(Right - Left)
    f1 = func(x1)
    f2 = func(x2)
    delta = dec(Right - Left)
    while delta > dec(e ** 2) and Left < Right:
        if f1 < f2:
            i = dec(FibonacciSequence(c) / FibonacciSequence(c + 2))
            c -= 1
            Right = x2
            x2 = x1
            x1 = Left + dec(Right - Left) * i
            f2 = f1
            f1 = dec(func(x1))
        else:
            i = dec(FibonacciSequence(c + 1) / FibonacciSequence(c + 2))
            c -= 1
            Left = x1
            x1 = x2
            x2 = Left + dec(Right - Left) * i
            f1 = f2
            f2 = dec(func(x2))
        delta = dec(Right - Left)
    return (Left + Right) / dec(2)

def GenericFunc(n, k):
    return n

def sravnenie(v1, v2):
    i = 0
    if(len(v1) != len(v2)):
        return False
    while i < len(v1):
        if(v1[i] != v2[i]):
            return False
    return True