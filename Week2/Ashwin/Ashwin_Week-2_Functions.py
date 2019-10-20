import numpy as np
def qubit():
    #checking Valadity
    if (np.absolute(complx_a))**2 + (np.absolute(complx_b)**2) ==1:
        #dot product
        ket=np.array([[complx_a], [complx_b]])
        print(f"Valid Qubit\n{ket}\n")
        #Transposing and conjugating
        bra= ket.conjugate().transpose()
        print(f"The transpose of the conjugate of {ket} is\n{bra}\n")
    else:
        print(f"Invalid Qubit\n{complx_a}\n{complx_b}\n")

def standard_basis(n):
    #creating an empty list
    s_matrix = []
    for bin_num in range(0, 2 ** n):
        #creating a list for every no in 2^n
        temp = []
        for digit in range(n):
            temp.insert(0, int((bin_num >> digit) % 2 == 1))
        s_matrix.append(temp)
        #converting list to array
    s_matrix = np.array(s_matrix)
    print(f"The no of Qubits are\n{s_matrix}\n")
    def measure_multiple():
        conjugate_s_matrix=s_matrix.conjugate().transpose()
        #dot product
        m_multiple=np.dot(s_matrix,conjugate_s_matrix)
        print(f"The inner product of the above matrix is\n{m_multiple}\n")
    def inner_product():
        ket = np.array([[complx_a], [complx_b]])
        bra = ket.conjugate().transpose()
        #dot product
        inner_p=np.dot(bra,ket)
        conjugate_s_matrix = s_matrix.conjugate().transpose()
        inner_p1=np.dot(s_matrix,conjugate_s_matrix)
        print(f"The inner product of\n{ket}\nand\n{bra} is\n\n{inner_p}\n")
        print((f"The inner product of\n{s_matrix}\nand\n{conjugate_s_matrix} is\n\n{inner_p1}\n"))
    #calling Nested functions
    measure_multiple()
    inner_product()

def density_matrix(complx_b,complx_a):
    #dot product
    d_matrix=np.dot(complx_b,complx_a)
    print(f"The Density Matrix of {complx_b} and {complx_a} is\n{d_matrix}\n")

try:
    #inputing values
    complx_a=complex(input("Enter a complex number (a+bj form)\n"))
    complx_b=complex(input("\nEnter a complex number (a+bj form)\n"))
    q_bit_no=int(input("\nEnter a number\n"))
    #calling Functions
    qubit()
    standard_basis(q_bit_no)
    density_matrix(complx_b,complx_a)
except:
    print(f"\nInvalid Complex number\n         OR\nInvalid Integer")
