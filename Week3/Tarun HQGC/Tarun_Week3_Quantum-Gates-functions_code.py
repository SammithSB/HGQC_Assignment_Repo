from Quantum_Gates import *
import numpy as np
from math import *
#
#
#1)checks if user defined quantum gate is valid or not
#
#
#function that executes the checking of quantum gates
def gate_check(fun):
    if np.all((np.matrix(fun))*(np.transpose(np.matrix(fun)))==(np.identity(fun.ndim))): #checking whether U*(conj.transpose(U)) = I 
        return 1
    else:
        return 0
if gate_check()==1:
    print("Valid Quantum Gate")
else:
    print("Not a valid Quantum Gate")
gate_check()#append details inside brackets as functions defined in other module as required
#
#
#2)Pauli X Quantum Gate:
#Pauli X quantum logic gate
#
#
#function that executes the pauli x gate
def pauli_x(ip):
    op=np.dot(pau_x,ip)
    return op
#input portion
dim=int(input('enter the dimension of the input qubit:'))  
print('you have to input 2^dim inputs and 1 arbitrary input')
ls=list()
for i in range(dim):
    ls.append(float(input('Enter:')))
    while i<=dim:                       #using dim as input for iterative limit, we can make a loop to append a list that is the converted to a matrix
        ls.append(float(input('Enter:')))
        i=i+1
ls.pop()
j=0
while j<=dim:
    l=np.matrix([ls,])
    j=j+1
#passing input into fun and simultaneously getting output
a=np.transpose(l)
b=(pauli_x(a))
print(b)
#
#
#3)Pauli Y Quantum Gate:
#Pauli Y quantum logic gate
#
#
#function that executes the pauli y gate
def pauli_y(ip):
    op=np.dot(pau_y,ip)
    return op
#input portion
dim=int(input('enter the dimension of the input qubit:'))  
print('you have to input 2^dim inputs and 1 arbitrary input')
ls=list()
for i in range(dim):
    ls.append(float(input('Enter:')))
    while i<=dim:                       #using dim as input for iterative limit, we can make a loop to append a list that is the converted to a matrix
        ls.append(float(input('Enter:')))
        i=i+1
ls.pop()
j=0
while j<=dim:
    l=np.matrix([ls,])
    j=j+1
#end of input portion
#passing input into pauli_y function and simultaneously getting output
a=np.transpose(l) #transposing matrix to make multiplication possible
b=(pauli_y(a))
print(b)
#
#
#4)Pauli Z Quantum Gate:
#Pauli Z quantum logic gate
#
#
#function that executes pauli z gates
def pauli_z(ip):
    op=np.dot(pau_z,ip)
    return op
#input portion
dim=int(input('enter the dimension of the input qubit:'))  
print('you have to input 2^dim inputs and 1 arbitrary input')
ls=list()
for i in range(dim):
    ls.append(float(input('Enter:')))
    while i<=dim:                       #using dim as input for iterative limit, we can make a loop to append a list that is the converted to a matrix
        ls.append(float(input('Enter:')))
        i=i+1
ls.pop()
j=0
while j<=dim:
    l=np.matrix([ls,])
    j=j+1
#end of input portion
#passing input into pauli_z and then getting output
a=np.transpose(l) #transposing matrix to make multiplication possible
b=(pauli_z(a))
print(b)
#
#
#5)CNOT Gate
#CNOT Quantum Logic gate
#
#
#function that executes CNOT gate
def contr_not(ip):
    op=np.dot(cnot(),ip)
    return op
#input portion
dim=int(input('enter the dimension of the input qubit:'))  
print('you have to input 2^dim inputs and 3 irrelevant inputs')
ls=list()
for i in range(dim):
    ls.append(float(input('Enter:')))
    while i<=dim:                       #using dim as input for iterative limit, we can make a loop to append a list that is the converted to a matrix
        ls.append(float(input('Enter:')))
        i=i+1
for k in range(1,(dim)+2):
    ls.pop()
j=0
while j<=dim:
    l=np.matrix([ls,])
    j=j+1
#passing input into contr_not and then getting output
a=np.transpose(l)#transposing matrix l so that matrix multiplication is possible 
b=(contr_not(a))
print(b)
#
#
#6)Toffoli Gate
#Toffoli Quantum Logic gate
#
#
#function that executes the toffoli gate:
def toffoli(ip):
    op=np.dot(tofo(),ip)
    return op
#input portion:
dim=int(input('enter the dimension of the input qubit:'))  
print('you have to input 2^dim inputs and 4 irrelevant inputs')
ls=list()
for i in range(dim):
    ls.append(float(input('Enter:')))
    while i<=dim:                   #using dim as input for iterative limit, we can make a loop to append a list that is the converted to a matrix
        ls.append(float(input('Enter:')))
        i=i+1
for k in range(1,(dim)+2):
    ls.pop()
j=0
while j<=dim:
    l=np.matrix([ls,])
    j=j+1
#end of input portion
#passing input into toffoli and then getting output
a=np.transpose(l)#transposing matrix l so that matrix multiplication is possible 
b=(toffoli(a))
print(b)
#
#
#7)Hadamard Gate:
#Hadamard Quantum logic Gate
#
#
#function that executes the gate:
def hadamard(ip):
    op=np.dot(hada(),ip)
    return op
#input portion
dim=int(input('enter the dimension of the input qubit:'))  
print('you have to input 2^dim inputs and 1 irrelevant input')
ls=list()
for i in range(dim):
    ls.append(float(input('Enter:')))
    while i<=dim:                       #using dim as input for iterative limit, we can make a loop to append a list that is the converted to a matrix
        ls.append(float(input('Enter:')))
        i=i+1
ls.pop()
j=0
while j<=dim:
    l=np.matrix([ls,])
    j=j+1
#passing input into hadamard and then getting output
a=np.transpose(l) #matrix transposing allows for matrix multiplication
b=(hadamard(a))
print(b)
#
#
#8)Swapping of Qubits with Hadamard and CNOT gates
#Qubit logic circuit imitated by program
#
#
#function that executes swapping of qubits
def qswap(ip,ip2):
    op1=np.outer(ip,ip2)
    op2=np.outer(cnot(),hada())
    op2=np.outer(op2,cnot())
    op2=np.outer(op2,hada())
    op2=np.outer(op2,cnot())
    op3=np.outer(op2,op1)
    return op3
#input portion
dim=int(input('enter the dimension of the input qubit 1:'))  
print('you have to input 2^dim inputs and 1 irrelevant inputs')
ls=list()
for i in range(dim):
    ls.append(float(input('Enter:')))
    while i<=dim:                       #using dim as input for iterative limit, we can make a loop to append a list that is the converted to a matrix
        ls.append(float(input('Enter:')))
        i=i+1
ls.pop()
j=0
while j<=dim:
    l=np.matrix([ls,])
    j=j+1
dim2=int(input('enter the dimension of the input qubit 2:'))# here we need two lists as we have two qubits to check for 
print('you have to input 2^dim inputs and 1 irrelevant inputs')
ls2=list()
for i in range(dim2):
    ls2.append(float(input('Enter:')))
    while i<=dim2:                      #using dim as input for iterative limit, we can make a loop to append a list that is the converted to a matrix
        ls2.append(float(input('Enter:')))
        i=i+1
ls2.pop()
j=0
while j<=dim2:
    l2=np.matrix([ls2,])
    j=j+1
#End of input portion
#passing input into qswap and then getting output
b=(qswap(l,l2))
print(b)


    

