import random
import numpy as np


# initialize_qubit(to_ket)
def qubit_to_ket(alpha, beta):
    qubit_ket = np.array([[alpha], [beta]])
    return qubit_ket


# check_func(to_ket)
print(qubit_to_ket(0+0.6j, 0-0.8j))


# initialize_qubit(to_bra)
def qubit_to_bra(alpha, beta):
    qubit_ket = qubit_to_ket(alpha, beta)
    qubit_bra = qubit_ket.conjugate().transpose()
    return qubit_bra


# check_func(to_bra)
print(qubit_to_bra(0+0.6j, 0-0.8j))


# check_validity
def check_valid_pair(alpha, beta):
    qubit_ket = qubit_to_ket(alpha, beta)
    qubit_bra = qubit_to_bra(alpha, beta)
    bra_ket = np.dot(qubit_bra, qubit_ket)
    if bra_ket[0] == 1:
        print('valid pair')
    else:
        print('invalid pair')


# check_func(valid_pair)
check_valid_pair(0+0.6j, 0-0.8j)
check_valid_pair(0+0.5j, 0-0.5j)


# construct_standard_basis for n qubits(binary_representation)
def construct_standard_basis(n):
    basis_vector_list = []
    for i in range(2**n):
        basis = '0'*(n-len(bin(i)[2:]))+bin(i)[2:]
        basis_vector_list.append(basis)
    return basis_vector_list


# check func(standard_basis)
print(construct_standard_basis(2))


# converting array to list
def convert(array):
    if np.size(array, axis=0) == 1:
        nest_l = array.tolist()
    elif np.size(array, axis=1) == 1:
        array_1 = array.transpose()
        nest_l = array_1.tolist()
    return nest_l[0]


# creating a combined state
def comb_state(qubit_st1, qubit_st2):
    qubit_st1_list = convert(qubit_st1)
    qubit_st2_row = qubit_st2.transpose()
    qubit_comb_state = []
    for i in range(len(qubit_st1_list)):
        qubit_comb_st_1 = convert(qubit_st1_list[i] * qubit_st2_row)
        qubit_comb_state = qubit_comb_state + qubit_comb_st_1
    comb_st_column = np.array([np.asarray(qubit_comb_state)])
    comb_st1 = comb_st_column.transpose()
    return comb_st1


# check func(combined_states)
qubit_1 = np.array([[0], [1]])
qubit_2 = np.array([[1], [0]])
print(comb_state(qubit_1, qubit_2))


# measuring_single_qubit
def measure_single_qubit(qubit1, general_st):
        measure_qubit_list = convert(np.dot(qubit1.transpose(), general_st))
        measure_qubit = measure_qubit_list[0]
        return measure_qubit


# check func(measure_single_qubit)
qubit_1 = np.array([[0.6], [0.8]])
qubit_2 = np.array([[1/2**4], [1/2**4]])
print(measure_single_qubit(qubit_1, qubit_2))


# measuring_multiple_qubits
def measure_multiple_qubits(qubits):
    n = len(convert(qubits))
    random_state = random.randint(2, n-1)
    if random_state == n-1:
        part_1 = convert(np.zeros([1, n-1], dtype=int))
        part_2 = [1]
        standard_st_list = part_1 + part_2
    else:
        part_1 = convert(np.zeros([1, random_state], dtype=int))
        part_2 = [1]
        part_3 = convert(np.zeros([1, n - random_state-1], dtype=int))
        standard_st_list = part_1 + part_2 + part_3
    standard_st = np.array([np.asarray(standard_st_list)])
    measure_qubit_list = convert(np.dot(qubits.transpose(), standard_st.transpose() ))
    measure_qubit = measure_qubit_list[0]
    return measure_qubit


# check func(measure_multiple_qubits)
qubit_1 = np.array([[0], [0], [1], [0]])
print(measure_multiple_qubits(qubit_1))