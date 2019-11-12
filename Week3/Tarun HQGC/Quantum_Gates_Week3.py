import numpy as np
import cmath 
from math import sqrt
def pau_x():
    p_x=np.array([[0,1],[1,0]])
    return p_x
def pau_y():
    p_y=np.array([[0,-(cmath.sqrt(-1))],[(cmath.sqrt(-1)),0]])
    return p_y
def pau_z():
    p_z=np.array([[1,0],[0,-1]])
    return p_z
def hada():
    h=(1/sqrt(2))*(np.array([[1,1],[1,-1]]))
    return h
def cnot():
    cn=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
    return cn
def tofo():
    tof=np.array([[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,0]])
    return tof
