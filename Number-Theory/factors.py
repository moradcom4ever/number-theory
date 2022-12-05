# Function to return the factors of 'n'
from array import array

print()
print("Function to return Factors of 'n'")
print()
arr = []


def factors(n):
    for i in range(n-1, 2, -1):
        if n % i == 0:
            arr.append(int(n/i))
            factors(i)
    arr.append(n)
    print()
    print(f"Factors of '{x}' are {arr}")
    print()
    quit()


x = int(input("Enter 'n' to find the factors : "))
factors(x)
