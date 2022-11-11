#Siddharth Tiwari B-3 
num1= int(input("Enter the First number\n"))
num2= int(input("Enter the Second number\n"))
if num1>num2:
    min = num1
else:
    min = num2
for i in range(1, min+1):
    if num1%i==0 and num2%i==0:
       gcd = i
print(f"The GCD of these two numbers is {gcd}")
// yes this is correct code and nicely implemented plan.
