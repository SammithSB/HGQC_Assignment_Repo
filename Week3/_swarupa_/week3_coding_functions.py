#assuming for single qbit state
#assuming that the three qubits on which the gates are to be applied are already declared by the user which are q1,q2,q3

from gates import* #this is to import all the variables from gates
import numpy as np
import math


#defining the functions to calculate the outputs
def check_validity(q1,q2,q3): #to check validity of qubit
	if(np.linalg.norm(q1,ord=2)==1 and np.linalg.norm(q2,ord=2)==1 and np.linalg.norm(q3,ord=2)==1):
		return 1
	else:
		print("qubit invalid, enter only valid qubits")
		exit()
def pauli_x_gate(q1):
	q1_x=np.matmul(x,q1)
	print("on applying pauli x on q1, we get: ",q1_x)
	return q1_x
def pauli_z_gate(q1):
	q1_z=np.matmul(z,q1)
	print("on applying pauli z on q1, we get: ",q1_z)
	return q1_z

def pauli_y_gate(q1):
	q1_y=np.matmul(y,q1)
	print("on applying pauli y on q1, we get: ",q1_y)
	return q1_y

def hadamard_gate(q1):
	q1_h=np.matmul(h,q1)
	print("on applying hadamard to q1, we get: ",q1_h)
	return q1_h
def cnot_gate(q1,q2):
	q1q2_combine=np.kron(q1,q2)
	cnot_output=np.matmul(cnot,q1q2_combine)
	print("the output after applying cnot gate to q1,q2 is: ",cnot_output)
	return cnot_output
def swap_gate(q1,q2):
	q1q2_combine=np.kron(q1,q2)
	swap_output=np.matmul(swap,q1q2_combine)
	print("the output after applying swap gate to q1,q2 is: ",swap_output)
	return swap_output
def controlled_z_gate(q1,q2):
	q1q2_combine=np.kron(q1,q2)
	cz_output=np.matmul(cz,q1q2_combine)
	print("the output after applying controlled z gate to q1,q2 is: ",cz_output)
	return cz_output
def controlled_x_gate(q1,q2):
	q1q2_combine=np.kron(q1,q2)
	cx_output=np.matmul(cx,q1q2_combine)
	print("the output after applying controlled x gate to q1,q2 is: ",cx_output)
	return cx_output
def t_gate(q1):
	q1_t=np.matmul(t,q1)
	print('the output after applyting a t gate to q1 is : ',q1_t)
	return q1_t
def s_gate(q1):
	q1_s=np.matmul(s,q1)
	print('the output after applying s gate to q1 is; ',q1_s)
	return q1_s
def toffoli_gate(q1,q2,q3):
	q1q2=np.kron(q1,q2)
	ten_pro=np.kron(q1q2,q3)
	tof_output=np.matmul(tof,ten_pro)
	print('the output after applying toffoli gate is: ',tof_output)
	return tof_output
#now, calling all the functions and printing the outputs
qubit1=np.array([[0.8],[0.6]])
qubit2=np.array([[0.2],[math.sqrt(0.96)]])
qubit3=np.array([[1],[0]])
check_validity(qubit1,qubit2,qubit3)
pauli_x_gate(qubit1)
pauli_y_gate(qubit3)
pauli_z_gate(qubit2)
hadamard_gate(qubit1)
cnot_gate(qubit2,qubit3)
swap_gate(qubit1,qubit2)
controlled_x_gate(qubit1,qubit3)
controlled_z_gate(qubit2,qubit3)
t_gate(qubit2)
s_gate(qubit1)
toffoli_gate(qubit1,qubit3,qubit2)


	
	
	


		
