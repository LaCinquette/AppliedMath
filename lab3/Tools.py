import numpy as np
import math
from scipy import sparse

def VectorDistance(A: np.ndarray, B: np.ndarray):
    res = 0
    for i in range(len(A)):
        res += (A[i][0] - B[i][0])**2
    res = math.sqrt(res)
    return res

def E1(n):
    ptrL = np.array([0] * (n + 1))
    indL = np.array([0] * n)
    dataL = np.array([1.] * n)
    for i in range(0, n + 1):
        ptrL[i] = i
    for i in range(0, n):
        indL[i] = i
    return sparse.csr_matrix((dataL, indL, ptrL), shape=(n, n))

def InverseMatrix(E):
    n = len(E.toarray())
    A = E.copy()
    L = E1(n)
    j = 0
    while j < n - 1:
        i = j + 1
        while i < n:
            k = 0
            h = A[i, j] / A[j, j]
            while k < n:
                A[i, k] -= A[j, k] * h
                L[i, k] -= L[j, k] * h
                k += 1
            i += 1
        j += 1
    return L

def peremnoj(A, x, d):
    n = len(x)
    otvet = np.array([0.] * n)
    i = 0
    while i < n:
        j = 0
        while j < n:
            otvet[i] += A[i, j] * x[j]
            j += 1
        otvet[i] += d[i]
        i += 1
    return otvet

def dist(a, b):
    h = 0.
    i = 0
    while i < len(a):
        h += (a[i] - b[i]) ** 2
        i += 1
    return h

def param(B):
    i = 0
    p = 0.
    while i < len(B.toarray()):
        s = 0
        j = 0
        while j < len(B.toarray()):
            s += abs(B[i, j])
            j += 1
        if(s > p):
            p = s
        i += 1
    return p