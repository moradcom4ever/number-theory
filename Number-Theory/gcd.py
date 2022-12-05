# Function to return gcd of a and b
print("Function to return GCD of 'a' and 'b'")
print()


def gcd(c, d):
    if c == 0:
        return d
    return gcd(d % c, c)


a = int(input("Enter first integer 'a' : "))
b = int(input("Enter second integer 'b' : "))
x = gcd(a, b)

print()
print("The result for GCD(" + str(a) + " , " + str(b) + ") is: " + str(x))
print()
