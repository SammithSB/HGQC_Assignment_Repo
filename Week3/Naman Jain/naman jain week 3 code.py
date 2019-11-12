import numpy as np
from qgates import *

def valid_qgate(a):
    try:
        if a.shape[0]==a.shape[1]:
            pass
    except:
        return 'Not valid'
    a_conj=a.conjugate().transpose()
    I_matrix=np.identity(a.shape[0],dtype=int)
    product=np.dot(a,a_conj)
    rev_product=np.dot(a_conj,a)
    if np.array_equal(a,a_conj) and np.array_equal(a_conj,a):
        return 'Valid'
    else:
        return 'Not Valid'

print(valid_qgate(random_matrix))


