import numpy as np
import math as ma
root = ma.sqrt(2))

#Hadamard Gate 

h=(1/root)*np.array([[1,1],[1,-1]])

#Pauli Gates

x=np.array([[0,1],[1,0]])

y=np.array([[0,-1j],[-1j,0]])

z=np.array([[1,0],[0,-1]])

#Swap Gate

swap=np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])

#Cnot Gate

cnot=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])

#Toffili Gate

tof=np.array([[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,1]])

#Controlled Pauli Gates

cz=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,-1]])

cx=np.array([[1,0,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,-1j]])

#Phase Gates

#S Gate
s=np.array([[1,0],[0,1j]])

#S-dagger Gate
sd=np.array([[1,0],[0,-1j]])

#T Gate
t=np.array([[1,0],[0,ma.e**((ma.pi/4)*1j)]])

#Tdagger Gate
td=np.array([[1,0],[0,ma.e**((ma.pi/4)*1j)]])


