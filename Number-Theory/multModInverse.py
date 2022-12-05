print()
print("Python3 program to find modular inverse of A under modulo M")
print("(A * A^-1) mod M = 1")
print()

def modInverse(A, M):
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1

A = int(input("Enter 'A' : "))
M = int(input("Enter 'M' : "))

r = modInverse(A,M)
print
print(f"Multiplicative Inverse for '{A}' under modulo '{M}' = {r}")
print()