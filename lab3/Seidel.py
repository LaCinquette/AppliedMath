import numpy as np
from CSRMatrixGeneration import GenerateCSRMatrix
from Tools import *


def Seidel(matrix, b, e):
    k = 0
    n = len(matrix.toarray())
    A = matrix.copy()
    B = GenerateCSRMatrix(n)
    d = np.array([0.] * n)  # x(n+1) = Bx(x) + d
    i = 0
    while i < n:
        j = 0
        while j < n:
            if (i == j):
                B[i, j] = 0
            else:
                B[i, j] = -A[i, j] / A[i, i]
            j += 1
        d[i] = b[i] / A[i, i]
        i += 1
    x = np.array([0.] * n)
    x_new = np.array([0.] * n)
    i = 0
    while i < n:
        j = 0
        while j < i:
            x_new[i] += B[i, j] * x_new[j]
            j += 1
        while j < n:
            x_new[i] += B[i, j] * x[j]
            j += 1
        x_new[i] += d[i]
        i += 1
    k += 1
    E = (1 - param(B)) / param(B) * e
    while dist(x, x_new) > E ** 2:
        x = x_new
        x_new = np.array([0.] * n)
        i = 0
        while i < n:
            j = 0
            while j < i:
                x_new[i] += B[i, j] * x_new[j]
                j += 1
            while j < n:
                x_new[i] += B[i, j] * x[j]
                j += 1
            x_new[i] += d[i]
            i += 1
        k += 1
        if k > 10000000:
            return "Error"
    print("Seidel", k)
    return x_new

def SeidelIterations(matrix, b, e):
    k = 0
    n = len(matrix.toarray())
    A = matrix.copy()
    B = GenerateCSRMatrix(n)
    d = np.array([0.] * n)  # x(n+1) = Bx(x) + d
    i = 0
    while i < n:
        j = 0
        while j < n:
            if (i == j):
                B[i, j] = 0
            else:
                B[i, j] = -A[i, j] / A[i, i]
            j += 1
        d[i] = b[i] / A[i, i]
        i += 1
    x = np.array([0.] * n)
    x_new = np.array([0.] * n)
    i = 0
    while i < n:
        j = 0
        while j < i:
            x_new[i] += B[i, j] * x_new[j]
            j += 1
        while j < n:
            x_new[i] += B[i, j] * x[j]
            j += 1
        x_new[i] += d[i]
        i += 1
    k += 1
    E = (1 - param(B)) / param(B) * e
    while dist(x, x_new) > E ** 2:
        x = x_new
        x_new = np.array([0.] * n)
        i = 0
        while i < n:
            j = 0
            while j < i:
                x_new[i] += B[i, j] * x_new[j]
                j += 1
            while j < n:
                x_new[i] += B[i, j] * x[j]
                j += 1
            x_new[i] += d[i]
            i += 1
        k += 1
        if k > 10000000:
            return "Error"
    #k = math.ceil(math.log10((1.0-param(B))*e/float(max(abs(d))))/math.log10(float(param(B))) - 1)
    #print("Seidel", k)
    return k

def SeidelMethod_iterations(coefs_matrix, results_vector, eps):
    iterations = 0
    A = coefs_matrix.copy().toarray()
    B = results_vector.copy()
    Beta = B.copy()
    Alpha = A.copy()

    for i in range(len(Beta)):
        Beta[i][0] = B[i][0]/A[i][i]
    
    for i in range(len(Alpha)):
        for j in range(len(Alpha[i])):
            Alpha[i][j] = -A[i][j]/A[i][i]
            if(i == j):
                Alpha[i][j] = 0
    
    X = Beta.copy()
    res = X.copy()
    for i in range(0, len(res)):
        iterations += 1
        res[i][0] = Beta[i][0] + sum([Alpha[i][j]*res[j][0] for j in range(i)]) + sum([Alpha[i][j]*X[j][0] for j in range(i, len(X))])
    
    while(VectorDistance(res, X) > eps):
        X = res.copy()
        for i in range(0, len(res)):
            iterations += 1
            res[i][0] = Beta[i][0] + sum([Alpha[i][j]*res[j][0] for j in range(i)]) + sum([Alpha[i][j]*X[j][0] for j in range(i, len(X))])
    
    return iterations