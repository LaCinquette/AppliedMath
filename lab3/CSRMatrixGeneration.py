from Tools import *
import numpy as np
from scipy import sparse
import random
'''
def GenerateCSRMatrix(n: int):
    #n = random.randint(2, 20) # размерность матрицы
    matrix_as_list = []
    for i in range(n):
        row = []

        for j in range(n):
            if random.random() < 0.1 and i != j: # степень разреженности
                element = float(random.randint(-30, 30))
                if element == 0.0:
                    element = 1.0
                row.append(element)
            else:
                row.append(0.0)

        if sum(row) == 0.0:
            index = random.randint(0, n-1)
            if index == i:
                if index == n - 1:
                    index -= 1
                else:
                    index += 1
            element = float(random.randint(-30, 30))
            if element == 0.0:
                element = 1.0
            row[index] = element
            
        row[i] = sum([abs(a) for a in row]) + float(random.randint(1, 10))
        matrix_as_list.append(row)
    
    return sparse.csr_matrix(matrix_as_list)
'''
#print(GenerateCSRMatrix(10).toarray())

def GenerateCSRMatrix(k):
    A = sparse.csr_matrix(([], [], [0] * (k + 1)), shape=(k, k), dtype=np.float64)
    for i in range(k):
        n = 0
        for j in range(k):
            if i == j:
                A[i, j] = k + 1
            else:
                if n < 3:
                    A[i, j] = 1
                    n += 1
    return A
