# Python program to find GCD of two numbers

# define a function
def compute_gcd(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i 
    return gcd

num1 = 54 
num2 = 24

print("The G.C.D. is", compute_gcd(num1, num2))
