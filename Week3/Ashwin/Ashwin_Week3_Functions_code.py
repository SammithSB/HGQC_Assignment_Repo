import numpy as np

def valid_gate(mat):
    #mat is an array (matrix)
    #dagger form of mat
    mat_dagger= mat.transpose().conjugate()
    #checking UU*=U*U==I
    if np.linalg.det(np.dot(mat,mat_dagger))==1 and np.linalg.det(np.dot(mat_dagger,mat)) ==1:
        return True
    else:
        print(f"The gate\n{mat} is an invalid gate\n")
#checking validity of qubit
def valid_qubit(matrix):
    val_qbit=np.dot((matrix.transpose().conjugate()),matrix)
    if np.round(val_qbit[0])==1:
        return True
#defining Pauli X
def pauli_x(matrix):
    #pauli x gate matrix
    x=np.array([[0,1],[1,0]])
    #Checking validity of pauli x gate
    if valid_gate(x):
        print(f"The Pauli X Gate Matrix is\n{x}\n")
        #checking valid qubit
        if valid_qubit(matrix):
            final_state=np.dot(x,matrix)
            print(f"The Final state of the Qubit is\n{final_state}\n")
#defining Pauli Y
def pauli_y(matrix):
    #pauli Y gate matirx
    y=np.array([[0,-1j],[1j,0]])
    #checking validity of pauli y gate
    if valid_gate(y):
        print(f"The Pauli Y Gate Matrix is\n{y}\n")
        #checking validity of qubit
        if valid_qubit(matrix):
            final_state=np.dot(y,matrix)
            print(f"The Final state of the qubit is\n{final_state}\n")
#defining Pauli Z
def pauli_z(matrix):
    #pauli Z gate matrix
    z=np.array([[1,0],[0,-1]])
    #checking validity of pauli z gate
    if valid_gate(z):
        print(f"The Pauli Z Gate Matrix is\n{z}\n")
        #checking valid qubit
        if valid_qubit(matrix):
            final_state=np.dot(z,matrix)
            print(f"The Final state of the qubit is\n{final_state}\n")
#defining Hadamard gate
def hadamard(matrix):
    #hadamard gate matrix
    h=(1/np.sqrt(2))*np.array([[1,1],[1,-1]])
    #checking validity of qubit
    if valid_qubit(matrix):
        print(f"The Hadamard Gate Matrix is\n{h}\n")
        final_state=np.dot(h,matrix)
        print(f"The Final state of the qubit is\n{final_state}\n")
#defining CNOT gate
def cnot(target,control):
#target and control are arrays
    #CNOT gate matrix
    cn=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
    #checking validity of cnot gate
    if valid_gate(cn):
        print(f"The CNOT Gate Matrix is\n{cn}\n")
        #checking validity od qubit
        if valid_qubit(target) and valid_qubit(control):
            #operations on cnot gate matrix
            comb_state=np.kron(control,target)
            final_state=np.dot(cn,comb_state)
            print(f"The Final state of the Qubit is\n{final_state}\n")

#defining toffoli gate
def toffoli(target,control_a,control_b):
    #toffoli Gate matrix
    tof=np.array([[1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0]])
    #checking validity of toffoli gate
    if valid_gate(tof):
        print(f"The Toffoli Gate Matrix is\n{tof}\n")
        #checking valid qubit
        if valid_qubit(target) and valid_qubit(control_a) and valid_qubit(control_b):
            #operations on toffoli gate matrix
            final_control=np.kron(control_a,control_b)
            comb_state=np.kron(final_control,target)
            final_state=np.dot(tof,comb_state)
            print(f"The Final State of The Qubit id\n{final_state}\n")
#defining swap gate
def swap(matrix_1,matrix_2):
    #swap gate matrix
    sw=np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
    if valid_gate(sw):
        print(f"The Swap Gate Matrix is\n{sw}\n")
        if valid_qubit(matrix_1) and valid_qubit(matrix_2):
            #operations on Swap gate matrix
            comb_state=np.kron(matrix_1,matrix_2)
            final_state=np.dot(sw,comb_state)
            print(f"The Final state of the Qubit is\n{final_state}\n")
#defining combining gates
def combine_gates(gate1,gate2):
    if valid_gate(gate1) and valid_gate(gate2):
        #tensor product
        comb_gate=np.kron(gate1,gate2)
        print(f"The Combined Gate of\n{gate1} and\n{gate2} is\n\n{comb_gate}\n")
# defining combining qubits
def combine_qubits(qubit_a, qubit_b):
        if valid_qubit(qubit_a) and valid_qubit(qubit_b):
            # tensor product
            comb_qbit = np.kron(qubit_a, qubit_b)
            print(f"The combined state of the qubits\n{qubit_a} and\n{qubit_b} is\n\n{comb_qbit}\n")
#operating on combined gates
def operation_combine_gates(gate_1,gate_2,qubit_1,qubit_2):
        #checking valid gates
        if valid_gate(gate_1) and valid_gate(gate_2):
            #tensor product
            comb_gate=np.kron(gate_1,gate_2)
            #checking valid qubits
        if valid_qubit(qubit_1) and valid_qubit(qubit_2):
            #tensor product
            comb_qbit=np.kron(qubit_1,qubit_2)
        #tensor product of combined gates and combined qubits
        combined_gate_qubit_state=np.dot(comb_gate,comb_qbit)
        print(f"The Final State of the Qubit is\n{combined_gate_qubit_state}\n")

#calling Functions
#Checking if CNOT matrix is a valid gate or not
print(f"\nValidity of the gate is {valid_gate(np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]]))}\n")
pauli_x(np.array([[0],[1]]))
pauli_y(np.array([[1],[0]]))
pauli_z(np.array([[0],[1]]))
hadamard(np.array([[1],[0]]))
cnot(np.array([[1],[0]]),np.array([[0],[1]]))
toffoli(np.array([[1],[0]]),np.array([[1],[0]]),np.array([[0],[1]]))
swap(np.array([[1],[0]]),np.array([[0],[1]]))
combine_gates(np.array([[0,1],[1,0]]),np.array([[1,0],[0,-1]]))
combine_qubits(np.array([[0],[1]]),np.array([[1],[0]]))
operation_combine_gates(np.array([[0,1],[1,0]]),np.array([[1,0],[0,1]]),np.array([[1],[0]]),np.array([[0],[1]]))
