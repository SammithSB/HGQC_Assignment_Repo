import numpy as np
import math


# checking validity
def gate_validator(Q):
    Q1=Q.conjugate().transpose()
    Q2=np.array([[1,0],[0,1]])
    if np.dot(Q,Q1).all()==Q2:
        print('valid')
    else:
        print('invalid')
        
        
        
#defining pauli X gate
def pauli_X(Q):
    X=np.array([[0,1],[1,0]])
    return np.matmul(X,Q)


# defining pauli Y gate
def pauli_Y(Q):
    Y=np.array([[0,-1j],[1j,0]])
    return np.matmul(Y,Q)



# defining pauli Z gate
def pauli_Z(Q):
    Z=np.array([[1,0],[0,-1]])
    return np.matmul(Z,Q)


# defining Hadamard gate
def H(Q):
    H=np.array([[1/math.sqrt(2),1/math.sqrt(2)],[1/math.sqrt(2),-1/math.sqrt(2)]])
    return np.matmul(H,Q)



# defining CNOT gate
# enter Q as crossproduct of the two qubits i.e np.kron(qubit,qubit2)
def CNOT(Q):
    CNOT=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
    return np.matmul(CNOT,Q)



# defining CCNOT gate(type1)
# take crossproduct first two qubits as np.kron(qubit1,qubit2) and then take crossproduct of the result with third qubit in the same way as done before
def CCNOT1(Q):
    CCNOT=np.array([[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,0]])
    return np.matmul(CCNOT1,Q)



# defining CCNOT gate(type2)
# enter three qubits in the function
def CCNOT2(Q1,Q2,Q3):
    CCNOT=np.array([[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,0]])
    Q=np.kron(Q1,Q2)
    Q=np.kron(Q,Q3)
    return np.matmul(CCNOT2,Q)


# defining swap gate(type1)
def SWAP1(Q1,Q2):
    SWAP1=np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
    Q=np.kron(Q1,Q2)
    return np.matmul(Q,SWAP1)


# defining swap gate(type2)
# Q=np.kron(Q1,Q2)
def SWAP2(Q):
    SWAP2=np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
    return np.matmul(Q,SWAP2)



# Combining gates

def XZ(Q):
    XZ=pauli_X(pauli_Z(Q))
    return XZ

def YZ(Q):
    YZ=pauli_Y(pauli_Z(Q))
    return YZ

def XY(Q):
    XY=pauli_X(pauli_Y(Q))
    return XY
    
def HX(Q):
    HX=pauli_H(pauli(X(Q)))
    return HX

def HY(Q):
    HY=pauli_H(pauli(Y(Q)))
    return HY

def HZ(Q):
    HX=pauli_H(pauli(Z(Q)))
    return HZ


