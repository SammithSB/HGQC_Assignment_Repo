import numpy as np
import matplotlib as mpl

def initialise_basis():
    basis_0=np.array([[1],[0]])
    basis_1=np.array([[0],[1]])
    return basis_0,basis_1

def initialise_qubit():
    alpha=int(input("enter the value of alpha"))
    beta=int(input("enter the value of beta"))

def to_ket():
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

