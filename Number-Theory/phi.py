# A simple Python3 program to calculate phi(n) using Euler's Totient Function
print("A simple Python3 program to calculate Euler's Totient Function")
print()

arr = [1]

# Function to return gcd of a and b
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)

# A simple method to evaluate Euler Totient Function
def phi(n):
	result = 1
	for i in range(2, n):
		if (gcd(i, n) == 1):
			result += 1
			arr.append(i)
	return result

# Driver Code
x = int(input("Enter 'n' to calculate phi(n) : "))
print()
print("phi(" + str(x) + ") = " + str(phi(x)))
print()
print(arr)
print()