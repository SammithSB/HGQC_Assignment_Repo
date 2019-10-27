import math 
import numpy as np
#pauli gates
#x
x=np.array([[0,1],[1,0]])
#y gate
y=np.array([[0,-1j],[-1j,0]])
#z gate
z=np.array([[1,0],[0,-1]])

#hadamard gate H
h=(1/math.sqrt(2))*np.array([[1,1],[1,-1]])

#phase gates
#s gate
s=np.array([[1,0],[0,1j]])
#s dagger gate
sd=np.array([[1,0],[0,-1j]])
#t gate
t=np.array([[1,0],[0,math.e**((math.pi/4)*1j)]])
#t dagger gate
td=np.array([[1,0],[0,math.e**((math.pi/4)*1j)]])

#identity matrix
i=np.array([[1,0],[0,1]])

#swap gate
swap=np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])

#controlled not or cnot gate
cnot=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])

#doubly controlled not or toffili gate
tof=np.array([[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,1]])

#controlled pauli gates
#z
cz=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,-1]])
#x
cx=np.array([[1,0,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,-1j]])




