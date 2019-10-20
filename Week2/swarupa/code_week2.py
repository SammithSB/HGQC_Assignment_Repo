import numpy as np
import matplotlib as mpl
import cmath
from itertools import permutations
def initialize_basis():
    basis_0=np.array([[1],[0]])
    basis_1=np.array([[0],[1]])
    return basis_0,basis_1
def initialize_qubit()
    alpha_real=int(input("enter real no of alpha"))
    alpha_img=int(input("enter imaginary part of alpha"))
    beta_real=int(input("enter real part of beta"))
    beta_img=int(input("enter imaginary part of beta"))
    alpha=complex(alpha_real,alpha_img)
    beta=complex(beta_real,beta_img)
def to_ket(alpha,beta):
    ket=np.array([[alpha],[beta]])
    return ket
def to_bra():
    ket=to_ket()
    bra=ket.conjugate().transpose()
    return bra
def inner_product(m1,m2):
    inner_pro=np.dot(m1,m2)
    return inner_pro
def check_validity():
    inner_pro=inner_product(alpha,beta)
    if inner_pro==1:
        print('valid')
        return 1
    else:
        print('invalid')
    def construct_standard_basis(n):
    perm=permutations([1,0],n)
    lst=list(perm)
    for i in lst
        if (sum(lst[i]!=1)):
            lst.remove(lst[i])
    return lst
def combine_qbits():
    tensor_product=np.tensordot((alpha,beta) axes=([1,0],[0,1]))
    return tensor_product
def measure_single():
    prob_1=alpha**2
    prob_2=beta**2
def measure_multi(qubit_state):
    no=random.randint(0,n)
    lst1=lst[no]
    measure_mqubit=np.dot(lst1,qubit_state)
    return measure_mqubit
    
