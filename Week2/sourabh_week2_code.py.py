import numpy as np
import matplotlib as mpl
import cmath

def initialise_basis():
    basis_0=np.array([[1],[0]])
    basis_1=np.array([[0],[1]])
    return basis_0,basis_1
def initialise_qubit():
    alpha_real=int(input("enter the real part of alpha"))
    alpha_i=int(input("enter the imaginary part of alpha"))
    beta_real=int(input("enter the real part of beta"))
    beta_i=int(input("enter the imaginary part of beta"))
    alpha=complex(alpha_real,alpha_i)
    beta=complex(beta_real,beta_i)

def to_ket(alpha,beta):
    ket=np.array([[alpha],[beta]])
    return ket

def to_bra():
    ket=to_ket()
    bra=ket.conjugate().transpose()
    return bra

def check_validity():
    p=(alpha**2)+(beta**2)
    if p==1:
        print("valid")
    else:
        print("invalid")

def combine_qubits():
    tensor_product=np.tensordot((alpha,beta), axes=([1,0],[0,1]))
    return tensor_product

