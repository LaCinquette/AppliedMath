import numpy as np

from LU import LU

def SLE(A, d):
    iterations = 0
    n = len(A.toarray())
    listLU = LU(A) #Ax=b
    L = listLU[0]
    U = listLU[1]
    #LUx=b Ly=b Ux=y
    y = np.array([0.] * n)
    for i in range(0, n):
        if i == 0:
            y[i] = d[0]
        else:
            sum = 0
            for k in range(0, i):
                iterations += 1
                sum += L[i, k] * y[k]
            y[i] = d[i] - sum

    x = np.array([0.] * n)
    i = n-1
    while i >= 0:
        if i == n-1:
            x[i] = y[i]/U[i, i]
        else:
            sum = 0
            for k in range(i+1, n):
                iterations += 1
                sum += U[i, k] * x[k]
            x[i] = (y[i] - sum) / U[i, i]
        i -= 1
    return x

def SLE_iterations(A, d):
    iterations = 0
    n = len(A.toarray())
    listLU = LU(A) #Ax=b
    L = listLU[0]
    U = listLU[1]
    #LUx=b Ly=b Ux=y
    y = np.array([0.] * n)
    for i in range(0, n):
        if i == 0:
            y[i] = d[0]
        else:
            sum = 0
            for k in range(0, i):
                iterations += 1
                sum += L[i, k] * y[k]
            y[i] = d[i] - sum

    x = np.array([0.] * n)
    i = n-1
    while i >= 0:
        if i == n-1:
            x[i] = y[i]/U[i, i]
        else:
            sum = 0
            for k in range(i+1, n):
                iterations += 1
                sum += U[i, k] * x[k]
            x[i] = (y[i] - sum) / U[i, i]
        i -= 1
    return iterations