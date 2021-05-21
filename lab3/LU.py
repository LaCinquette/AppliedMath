from Tools import *

def LU_iterations(matrix):
    iterations = 0
    n = len(matrix.toarray())
    A = matrix.copy()
    L = E1(n)
    k = 0
    while k < n - 1:
        i = k + 1
        while i < n:
            j = k
            h = A[i, k]/A[k, k]
            while j < n:
                iterations += 1
                A[i, j] = A[i, j] - A[k, j] * h
                L[i, j] = L[i, j] - L[k, j] * h
                j += 1
            i += 1
        k += 1
    U = A
    A = L
    L = E1(n)
    k = 0
    while k < n - 1:
        i = k + 1
        while i < n:
            j = k
            h = A[i, k] / A[k, k]
            while j < n:
                iterations += 1
                A[i, j] = A[i, j] - A[k, j] * h
                L[i, j] = L[i, j] - L[k, j] * h
                j += 1
            i += 1
        k += 1
    i = 0

    return iterations #[L, U]

def LU(matrix):
    iterations = 0
    n = len(matrix.toarray())
    A = matrix.copy()
    L = E1(n)
    k = 0
    while k < n - 1:
        i = k + 1
        while i < n:
            j = k
            h = A[i, k]/A[k, k]
            while j < n:
                iterations += 1
                A[i, j] = A[i, j] - A[k, j] * h
                L[i, j] = L[i, j] - L[k, j] * h
                j += 1
            i += 1
        k += 1
    U = A
    A = L
    L = E1(n)
    k = 0
    while k < n - 1:
        i = k + 1
        while i < n:
            j = k
            h = A[i, k] / A[k, k]
            while j < n:
                iterations += 1
                A[i, j] = A[i, j] - A[k, j] * h
                L[i, j] = L[i, j] - L[k, j] * h
                j += 1
            i += 1
        k += 1
    i = 0
    #print("LU", iterations)

    return [L, U]