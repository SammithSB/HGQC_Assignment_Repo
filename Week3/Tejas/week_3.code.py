import numpy as np


#check validity of given gate
def check_validity_gate(gate):#the argument is a array
    hermitian_gate = gate.transpose().conjugate()
    # throught determinant method
    if np.linalg.det(np.dot(hermitian_gate, gate)) == 1.0:
        return True
    else:
        return False


#checking the function
if check_validity_gate(np.array([[0,1],[1,0]])):
     print("it's valid")
else:
    print("it's not valid")


#checking validity of a qubit
def check_validity(qubit):# the arugment is a column vector
        bra_ket =  np.dot(qubit.transpose().conjugate(), qubit)
        if bra_ket[0] == 1 or round(float(bra_ket[0]), 2) == 1.00:
            return True
        else:
            return False


#creating pauli X Gates
def pauli_X(qubit):# the argument is column vector
    if check_validity(qubit):
        return np.dot(np.array([[0, 1],[1, 0]]),qubit)
    else:
        print('invalid input')


#checking function
print(pauli_X(np.array([[0], [1]])))
print()

#creating pauliY gate
def pauli_Y(qubit):
    if check_validity(qubit):
        return np.dot(np.array([[0, -1j], [-1j, 0]]), qubit)
    else:
        print('invalid input')

#checking function
print(pauli_Y(np.array([[1], [0]])))
print()


#creating pauli_Z
def pauli_Z(qubit):
    if check_validity(qubit):
        return np.dot(np.array([[1, 0], [0, -1]]), qubit)
    else:
        print('invalid input')


#checking function
qubit = np.array([[1/2**0.5], [1/2**0.5]])
print(pauli_Z(qubit))
print()


# creating hadamard gate
def hadamard_gate(qubit):
    H = (1/np.sqrt(2))*np.array([[1, 1], [1, -1]])
    if check_validity(qubit):
        return np.dot(H, qubit)
    else:
        print('invalid input')

#checking the function
qubit = np.array([[1/np.sqrt(2)], [1/np.sqrt(2)]])
print(hadamard_gate(qubit))
print()


#creating controlled not gate
def cnot(control, target):
    Cnot = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    combined = np.kron(control, target)
    return np.dot(Cnot, combined)


#checking the function
control = np.array([[0], [1]])
target = np.array([[0], [1]])
print(cnot(control, target))
print()


#creating double controlled not gate
def ccnot(control_1,control_2,traget):
    Ccnot = np.array([[1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0]])
    control = np.kron(control_1, control_2)
    combined = np.kron(control, traget)
    return np.dot(Ccnot, combined)

#checking the function
control_1 = np.array([[0], [1]])
control_2 = np.array([[0], [1]])
target = np.array([[0], [1]])
print(ccnot(control_1, control_2, target))
print()


#creating controlled Pauli_Z gate
def cz(control, target):
    Cz = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0,  0, -1]])
    combined = np.kron(control, target)
    return np.dot(Cz, combined)


#checking the function
control = np.array([[0], [1]])
target = np.array([[0], [1]])
print(cz(control, target))
print()


#creating swap gate
def swap(qubit_1,qubit_2):
    Swap = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
    combined = np.kron(qubit_1, qubit_2)
    return np.dot(Swap, combined)


#checking the function
qubit_1 = np.array([[0], [1]])
qubit_2 = np.array([[1], [0]])
print(swap(qubit_1,qubit_2))
print()


#creating controlled swap gate, Fredkin gate
def cswap(control,traget_1,traget_2):
    Cswap = np.array([[1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1]])
    combined_1 = np.kron(control, traget_1)
    combined = np.kron(combined_1, traget_2)
    return np.dot(Cswap, combined)


#checking the function
control = np.array([[0], [1]])
target_1 = np.array([[0], [1]])
target_2 = np.array([[1], [0]])
print(cswap(control, target_1, target_2))
print()


#creating a function for combing gates
def combine_gate(*gates):#the arguments are array of gates in order
    combined = gates[0]
    for i in range(len(gates)-1):
        combined_1 = np.kron(combined, gates[i + 1])
        combined = combined_1
    return combined


#creating a function for combing qubits
def combine_qubits(*qubits):#the arguments are array of qubits in otder
    combined = qubits[0]
    for i in range(len(qubits)-1):
        combined_1 = np.kron(combined, qubits[i + 1])
        combined = combined_1
    return combined


#creating the controlled pauli Z using above function
Z = np.array([[1, 0], [0, -1]])
I = np.array([[1, 0], [0, 1]])
gates = combine_gate(I, Z,)
qubit_1 = np.array([[0], [1]])
qubit_2 = np.array([[1], [0]])
qubits = combine_qubits(qubit_1, qubit_2)
gates_1 = np.dot(gates,qubits)
Cnot = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
print('this is from combined state form\n', np.dot(Cnot,gates_1))
print('this is from controlled pauli_Z\n', cz(qubit_1, qubit_2))
