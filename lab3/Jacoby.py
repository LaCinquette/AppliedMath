import numpy as np

from CSRMatrixGeneration import GenerateCSRMatrix
from Tools import *


def Jacody(matrix, b, e):
    k = 0
    n = len(matrix.toarray())
    A = matrix.copy()
    B = GenerateCSRMatrix(n)
    d = np.array([0.] * n) # x(n+1) = Bx(x) + d
    i = 0
    while i < n:
        j = 0
        while j < n:
            if(i == j):
                B[i, j] = 0
            else:
                B[i, j] = -A[i, j]/A[i, i]
            j += 1
        d[i] = b[i]/A[i, i]
        i += 1
    x = d.copy()
    x_new = peremnoj(B, x, d)
    k += 1
    E = ( 1 - param(B))/param(B) * e
    while dist(x, x_new) > E ** 2:
        x = x_new
        x_new = peremnoj(B, x, d)
        k += 1
        if k > 10000000:
            return "Error"
    #print("Jacoby", k)
    return x_new

def JacobyMethod(coefs_matrix, results_vector, eps):
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
    res = np.matmul(Alpha, X) + Beta
    iterations += 1
    while(VectorDistance(res, X) > eps):
        iterations += 1
        X = res.copy()
        res = np.matmul(Alpha, X) + Beta
    
    return res