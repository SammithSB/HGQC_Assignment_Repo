import numpy as np
import math

random_matrix=np.array([[0,1,0,1],[1,0,1,0]])

'''Pauli gates'''
X=np.array([[0,1],[1,0]])
Y=np.array([[0,1j],[-1j,0]])
Z=np.array([[1,0],[0,-1]])

'''Hadmard gate'''
H=1/math.sqrt(2)*np.array([[1,1],[1,-1]])

'''Controlled NOT - CNOT'''
CNOT=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])

'''Controlled Pauli Z - CZ'''
CZ=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,-1]])

'''Swap gate -S'''
S=np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])

'''Tofolli - CCNOT'''
CCNOT=np.array([[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0],
                [0,0,0,0,1,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,1]])

