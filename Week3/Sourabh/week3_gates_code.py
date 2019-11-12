import math
import numpy as np

"""X Pauli gate"""
x=np.array([[0,1],[1,0]])
"""Y Pauli gate"""
y=np.array([[0,-1j],[-1j,0]])
"""Z Pauli gate"""
z=np.array([[1,0],[0,-1]])

"""Hadamard gate"""
h=(1/np.sqrt(2))*np.array([[1,1],[1,-1]])

"""CNOT or Controlled X gate"""
cnot=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])

"""Swap gate"""
swap=np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])

"""Controlled Z"""
cz=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,-1]])

"""Toffoli gate"""
ccnot=np.array([[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,1,0,0][0,0,0,0,0,0,0,1],
[0,0,0,0,0,0,1,0]])

"""Fredkin gate"""
cswap=np.array([[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1]])

"""U3 gate"""
u=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])

"""Identity matrix"""
iden=np.array([[1,0],[0,1]])



def check_validity(q1,q2,q3):
    if(np.linalg.norm(q1,ord=2)==1 and np.linalg.norm(q2,ord=2)==1 and np.linalg.norm(q3,ord=2)==1)):
        return 1
    else:
        print("qubit invalid")
        exit()

def pauli_x(q1):
    q1_x=np.matmul(x,q1)
    print("output for q1 on x is",q1_x)
    return q1_x

def pauli_y(q1):
    q1_y=np.matmul(y,q1)
    print("output for q1 on y is",q1_y)
    return q1_y

def pauli_z(q1):
    q1_z=np.matmul(z,q1)
    print("output for q1 on z is",q1_z)
    return q1_z

def hadamard(q1):
    q1_h=np.matmul(h,q1)
    print("output for q1 on h is",q1_h)
    return q1_h

def cnot(q1,q2):
    q1q2=np.kron(q1,q2)
    cnot_op=np.matmul(cnot,q1q2)
    print("output for q1,q2 on cnot is",cnot_op)
    return cnot_op

def swap(q1,q2):
    q1q2=np.kron(q1,q2)
    swap_op=np.matmul(swap,q1q2)
    print("output for q1,q2 on swap is",swap_op)
    return swap_op

def controlled_z(q1,q2):
    q1q2=np.kron(q1,q2)
    cz_op=np.matmul(cz,q1)
    print("output for q1,q2 on cz is",cz_op)
    return cz_op

def toffoli(q1,q2,q3):
    q1q2=np.kron(q1,q2)
    q1q2q3=np.kron(q1q2,q3)
    ccnot_op=np.matmul(ccnot,q1q2q3)
    print("output for q1,q2,q3 on ccnot is",ccnot_op)
    return ccnot_op

def fredkin(q1,q2,q3):
    q1q2=np.kron(q1,q2)
    q1q2q3=np.kron(q1q2,q3)
    cswap_op=np.matmul(cswap,q1q2q3)
    print("output for q1,q2,q3 on cswap is",cswap_op)
    return cswap_op

def u3(q1,q2):
    q1q2=np.kron(q1,q2)
    u_op=np.matmul(u,q1)
    print("output for q1,q2 on u3 is",u_op)
    return u_op

def iden(q1):
    q1_iden=np.matmul(iden,q1)
    print("output for q1 on iden is",q1_iden)
    return q1_iden


q1=np.array(0.7,(0.51)**2)
q2=np.array(0,1)
q3=np.array(1,0)
check_validity(q1)
check_validity(q2)
check_validity(q3)
pauli_x(q1)
pauli_y(q1)
pauli_z(q1)
hadamard(q1)
cnot(q1,q2)
swap(q1,q2)
controlled_z(q1,q2)
toffoli(q1,q2,q3)
fredkin(q1,q2,q3)
u3(q1,q2)
iden(q1)
