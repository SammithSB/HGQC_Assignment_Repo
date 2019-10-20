import numpy as np
α=float(input('enter the coefficient of 0 in qubit: '))
β=float(input('enter the coefficient of 1 in qubit: '))
def initialise_qubit_to_ket(α,β):
    ket=np.array([[α],[β]])
    if α**2+β**2==1:
        return ket
    else:
        print('invalid value for qubits')
print(initialise_ket_qubit(α,β))
def initialise_qubit_to_bra(α,β):
    bra=np.array([[α],[β]]).conjugate().transpose()
    if α**2+β**2==1:
        return bra
    else:
        print('invalid value for qubit')
initialise_qubit_to_bra(α,β)

#construction of standard basis
n=int(input('enter the number of qubits: '))
num_of_basis=2**n    
def construct_standard_basis(n):
      for i in range(0,num_of_basis):
        basis = '0'*(n-len(bin(i)[2:]))+bin(i)[2:]
        print('|',basis,'>')
    return ' '
print(construct_standard_basis(n))



#finding inner product
α=float(input('enter value of coefficient of 0 of the qubit'))
β=float(input('enter value of coefficient of 1 of qubit'))
if α**2+β**2==1:
    ket=np.array([[0],[1]])
    bra=ket.conjugate().transpose()
    np.dot(bra,ket)
    print(np.dot(bra,ket))
else:
    print('enter value valid value of qubit')

    

    
    
#measuring qubit
α=float(input('enter value of coefficient of 0 of the qubit: '))
β=float(input('enter value of coefficient of 1 of qubit: '))
def measure_qubit(input_qubit,standard_state):
    input_qubit=np.array([[α],[β]])
    standard_state_qubit=np.array([[γ],[δ]])
    print(np.dot(input_qubit.conjugate().transpose(),general_state_qubit))
    return ' '
print(measure_qubit(input_qubit,[[1],[0]]))

#measuring multiple qubit
α=float(input('enter value of coefficient of first value in qubit'))
β=float(input('enter value of coefficient of second value in qubit'))
γ=float(input('enter value of coefficient of third value in qubit'))
δ=float(input('enter value of coefficient of fourth value in qubit'))
def measure_multiple_qubits(input_value,standard_value):
    input_value=np.array([[α],[β],[γ],[δ]])
    standard_state=np.arrar([[1],[0],[0],[0]])
    print(np.dot(input_state,standard_state))
print(measure_multiple_qubits(input_value,[[1],[0],[0],[0]]))

#finding density matrix of single qubit
α=float(input('enter value of coefficient of 0 of the qubit'))
β=float(input('enter value of coefficient of 1 of qubit'))
def find_density_matrix(α,β):
    if α**2+β**2==1:
        ket=np.array([[α],[β]])
        bra=ket.conjugate().transpose()
        np.dot(ket,bra)
        print(np.dot(ket,bra))
    else:
        print('enter value valid value of qubit')
print(find_density_matrix)
