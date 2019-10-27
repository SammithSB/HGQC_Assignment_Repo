from gates import*
import numpy as np
import math as ma

qbit1=np.array([[0.8],[0.6]])
qbit2=np.array([[0.5],[math.sqrt(0.75)]])
qbit3=np.array([[1],[0]])

def validity(q1,q2,q3):
       if(np.linalgnorm(q1,ord=2)==1 and (np.linalgnorm(q2,ord=2)==1 and (np.linalgnorm(q3,ord=2)==1):
          	 print("valid qubits")
       else:
	print("enter valid qubits")
	exit()
def pauli_x(q1):
	q1x=np.matmul(x,q1)
 	print(" on applying pauli X we get ", q1x)

def pauli_y(q1):
	q1y=np.matmul(y,q1)
 	print(" on applying pauli Y we get ", q1y)

def pauli_z(q1):
	q1z=np.matmul(z,q1)
 	print(" on applying pauli Z we get ", q1z)

def hadamard(q1):
	q1h=np.matmul(h,q1)
 	print(" on applying Hadamard gate we get ", q1h)

def cnot(q1,q2):
	combine=np.kron(q1,q2)
	cnot_output=np.matmul(cnot,combine)
	print("on applying cnot i=on q1 and q2 we get ",cnot_output)

def swap(q2,q3):
	combine=np.kron(q1,q2)
	swap_output=np.matmul(swap,combine)
	print("on applying swap on q2 and q3 we get ",swap_output)

def toffoli(q1,q2,q3):
	combine=np.kron(q1,q2)
	tensor=np.kron(combine,q3)
	tof_output=np.matmul(tof,tenosr)
	print("on applying Toffoli gate we get ",tof_output)

def controlled_x(q1,q2):
	combine=np.kron(q1,q2)
	cx_output=np.matmul(cx,combine)
	print("on applying Controlled X gatewe get ",cx_output)

def controlled_z(q1,q3):
	combine=np.kron(q1,q3)
	cz_output=np.matmul(cx,combine)
	print("on applying Controlled Z gatewe get ",cz_output)

#callin the functions
validity(qbit1,qbit2,qbit3)
pauli_x(qbit1)
pauli_y(qbit1)
pauli_z(qbit1)
hadamard(qbit1)
cnot(qbit1,qbit2)
swap(qbit2,qbit3)
toffoli(qbit1,qbit2,qbit3)
controlled_x(qbit1,qbit2)
controlled_z(qbit1,qbit3)


