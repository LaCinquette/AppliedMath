import numpy as np
from scipy import sparse

def GenerateGilbert(n):
    m = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            m[i][j] = 1.0 / (float(i) + float(j) + 1.0)
    return sparse.csr_matrix(m)

#print(GenerateGilbert(5).toarray())
#print(np.array([[a] for a in np.ones(5)]))