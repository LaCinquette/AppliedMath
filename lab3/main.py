from CSRMatrixGeneration import GenerateCSRMatrix
import numpy as np
from scipy import sparse
from Gilbert import *
from Jacoby import *
from Seidel import *
from LU import LU, LU_iterations
from SystemOfLinearEquations import SLE, SLE_iterations
import matplotlib.pyplot as plt
from CSRMatrixGeneration import *
import time


'''
coefs = [
    [10., -7., 0.],
    [-3., 6., 2.],
    [5., -1., 5.]
]
eqs = [
    [3.],
    [4.],
    [1.]
]
'''
#print(JacobyMethod(np.array(coefs), np.array(eqs), 0.001))
#print(SeidelMethod(np.array(coefs), np.array(eqs), 0.0001))

"""
indptr = np.array([0, 3, 6, 9])
indices = np.array([0, 1, 2, 0, 1, 2, 0, 1, 2])
data = np.array([1, 2, 1, 2, 1, 1, 1, -1, 2])
csr_mat = sparse.csr_matrix((data, indices, indptr), shape=(3,3))
"""




'''
a = np.array([[1, 2, 1],
             [2, 1, 1],
             [1, -1, 2]])

indptr = np.array([0, 2, 5, 8])
indices = np.array([0, 1, 0, 1, 2, 0, 1, 2])
data = np.array([10., -7, -3, 6, 2, 5, -1, 7])
csr_mat = sparse.csr_matrix((data, indices, indptr), shape=(3, 3))

d = np.array([3, 4, 1])
'''

X = [5*a for a in range(1, 21)]
Y = []
'''
for x in X:
    print(x)
    time_start = time.time()
    LU_iterations(GenerateCSRMatrix(x))
    time_end = time.time()    
    Y.append(time_end - time_start)
plt.figure(figsize=(9, 7))
plotLU = plt.plot(X, Y, label="LU")
plt.xticks(X)
plt.legend(handles=[plotLU[0]], title='Legend', bbox_to_anchor=(1.002, 1), loc='upper left')
plt.show()
'''
'''
Y.clear()
for x in X:
    print(x)
    Y.append(JacodyIterations(GenerateCSRMatrix(x), np.array([1.] * x), 0.001))
plt.figure(figsize=(9, 7))
plotLU = plt.plot(X, Y, label="Jacoby")
plt.xticks(X)
plt.legend(handles=[plotLU[0]], title='Legend', bbox_to_anchor=(1.002, 1), loc='upper left')
plt.show()

Y.clear()
for x in X:
    print(x)
    Y.append(SeidelIterations(GenerateCSRMatrix(x), np.array([1.] * x), 0.001))
plt.figure(figsize=(9, 7))
plotLU = plt.plot(X, Y, label="Seidel")
plt.xticks(X)
plt.legend(handles=[plotLU[0]], title='Legend', bbox_to_anchor=(1.002, 1), loc='upper left')
plt.show()


Y.clear()
for x in X:
    print(x)
    time_start = time.time()
    SLE_iterations(GenerateCSRMatrix(x), np.array([1.] * x))
    time_end = time.time()
    Y.append(time_end - time_start)
plt.figure(figsize=(9, 7))
plotLU = plt.plot(X, Y, label="SLE")
plt.xticks(X)
plt.legend(handles=[plotLU[0]], title='Legend', bbox_to_anchor=(1.002, 1), loc='upper left')
plt.show()
'''



'''
N = [10, 50, 100]
for n in N:
    print("Решается для n =", n)
    print("Jacoby", Jacody(GenerateCSRMatrix(n), np.array([1.] * n), 0.001))
    print("Seidel", SeidelIterations(GenerateCSRMatrix(n), np.array([1.] * n), 0.001))
    print("SLE", SLE_iterations(GenerateCSRMatrix(n), np.array([1.] * n)))
'''

Conds = []
XY = []
'''
Conds.clear()
Y.clear()
for x in X:
    A = GenerateGilbert(x)
    print(x)
    Conds.append(np.linalg.cond(A.toarray()))
    Y.append(Jacody(A, np.array([1.] * x), 0.001))

XY.clear()
for i in range(len(Conds)):
    XY.append((Conds[i], Y[i]))
XY.sort(key=lambda input: input[0])

plt.figure(figsize=(12, 7))
plotLU = plt.plot([a[0] for a in XY], [a[1] for a in XY], label="Jacoby")
#plt.xticks(X)
plt.legend(handles=[plotLU[0]], title='Legend', bbox_to_anchor=(1.002, 1), loc='upper left')
plt.show()
'''
'''
Conds.clear()
Y.clear()
for x in X:
    A = GenerateGilbert(x)
    print(x)
    Conds.append(np.linalg.cond(A.toarray()))
    Y.append(SeidelMethod_iterations(A, np.array([[a] for a in np.ones(x)]), 0.001))

XY.clear()
for i in range(len(Conds)):
    XY.append((Conds[i], Y[i]))
XY.sort(key=lambda input: input[0])

plt.figure(figsize=(12, 7))
plotLU = plt.plot([a[0] for a in XY], [a[1] for a in XY], label="Seidel")
#plt.xticks(X)
plt.legend(handles=[plotLU[0]], title='Legend', bbox_to_anchor=(1.002, 1), loc='upper left')
plt.show()
'''

'''
#listLU = LU(csr_mat)
#print(csr_mat)
#print()
#print(csr_mat.toarray())
#print(d)
# print(listLU[0].toarray())
# print(listLU[1].toarray())
#print(SLE(csr_mat, d))
print(Jacody(csr_mat, d, 0.0001))
print(Seidel(csr_mat, d, 0.0001))
'''
N = [2, 3, 5]

for n in N:
    gM = GenerateGilbert(n)
    print(gM.toarray())
    print(JacobyMethod(gM, np.array([[a] for a in np.ones(n)]), 0.001))