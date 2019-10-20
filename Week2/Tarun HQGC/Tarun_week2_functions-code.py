import numpy as np
#1)initialising a qubit:
def initialise_qubit():
    base_0=np.array([[1],[0]])
    base_1=np.array([[0],[1]])
    return base_0,base_1
basis_0,basis_1=initialise_qubit()
print('Qubit in state zero is:')
print(basis_0)
print('Qubit in state one is:')
print(basis_1)
#2) and 3)taking input qubit to convert to bra and ket form:
def to_ket(a,b):
    p_k=np.transpose(np.matrix([a,b]))
    return p_k
def to_bra(a,b):
    p_b=np.matrix([a,b])
    return p_b
α=float(input('Enter a value for α:'))
β=float(input('Enter a value for β:'))
psi_ket=to_ket(α,β)
psi_bra=to_bra(α,β)
print('psi in ket form is:')
print(psi_ket)
print('psi in bra form:')
print(psi_bra)
#4)taking inputs to check if they can form a qubit or not:
def check_validity(a,b):
    if((np.abs(a))**2)+((np.abs(b))**2)==1:
        print('A qubit is valid with these inputs of magnitudes for states 0 and 1 and it is:')
        print(np.array([[a],[b]]))
    else:
        print('Given inputs cannot form a qubit')
α=float(input('Enter the value for α:'))
β=float(input('Enter the value for β:'))
check_validity(α,β)
#5)taking inputs to find the inner product of two qubits
def inner_product(α,β,α1,β1):
    b=np.transpose(np.matrix([[α],[β]]))
    psi=np.array([[α1],[β1]])
    i_pro=(float(np.dot(b,psi)))**2
    print('The amount of b in psi is:',i_pro)
print('To find amount of b in psi:') 
α11=float(input('Enter the value for α for b:'))
β11=float(input('Enter the value for β for b:'))
α21=float(input('Enter the value for α for psi:'))
β21=float(input('Enter the value for β for psi:'))
inner_product(α11,β11,α21,β21)
#6)taking inputs to measure a single qubit with respect to another
def measure_single(α,β):
    g_s=np.transpose(np.matrix([[α],[β]]))
    psi=np.array([[α1],[β1]])
    meas_single=(float(np.dot(g_s,psi)))**2
    print('The amount of general state in psi is:',meas_single)
print('To find amount of general state in psi:') 
α11=float(input('Enter the value for α for general state:'))
β11=float(input('Enter the value for β for general state:'))
α21=float(input('Enter the value for α for psi:'))
β21=float(input('Enter the value for β for psi:'))
measure(α11,β11,α21,β21)
#7)taking inputs to measure multiple qubits with respect to a basis state
def measure_multiple(n):
    b_s_ls=[];psi_ls=[]
    while i<n:
        b_s_ls.append(float(input('Enter the value for α for a basis state:')))
        psi_ls.append(float(input('Enter the value for α for psi:')))
        i+=1
    b_s=np.array(b_s_ls)
    psi=np.array(psi_ls)
    meas_multi=(float(np.dot(b_s,psi)))**2
    print('the qubit measured',meas_multi,'for the input basis state values')
print('To find amount of a basis state in psi:') 
dim=int(input('Enter the number of dimensions required:'))
measure_multiple(dim)
#8)taking an input to find density matrix for a qubit
def costruct_density_matrix(c):
    if c==0:
        print(np.outer([1,0],[1,0]))
    elif c==1:
        print(np.outer([0,1],[0,1]))
cho=int(input('Choose a single qubit state:'))
construct_density_matrix(cho)
#9)taking inputs to combine n qubits
def combine_qubits(n):
    α=float(input('Enter the value for α for the first qubit:'))
    β=float(input('Enter the value for β for first qubit:'))
    α1=float(input('Enter the value for α for the second qubit:'))
    β1=float(input('Enter the value for β for the second qubit:'))
    ls=list(np.outer([α,β],[α1,β1]))
    i=0
    while i<(n-2):
        α2=float(input('Enter the value for α for the next qubit:'))
        β2=float(input('Enter the value for β for the next qubit:'))
        ls=list(np.outer([ls],[α2,β2]))
        i+=1
    comb_qb=np.array(ls)
    print(comb_qb)
dim=int(input('Enter number of dimensions'))
combine_qubits(dim)
#10)taking an input to find the standard basis states for n dimensional qubits
def standard_basis():
    i=0
    j=0
    while i<=(2**n):
        c=1
        ls=[]
        while j<=n:
            if j==c:
                ls.append(1)
            else:
                ls.append(0)
        print(np.array(ls))
dim=int(input('Enter the number of dimensions:'))
standard_basis(dim)



    
