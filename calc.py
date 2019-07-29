import math
print("  0 - add")
print("  1 - subract")
print("  2 - multiply")
print("  3 - divide")
print("  4 - exponents")
print("  5 - sqaure root")
print("  6 - factorials")
print("  7 - fibonacci")
print("Enter a number to choose an operation: \n")
op = input()

#fibonacci method
def Fibonacci(n): 
    if n < 0: 
        print("Enter a positive number: ") 
    elif n == 1: 
        return 0
    elif n == 2: 
        return 1
    else: 
        return Fibonacci(n-1) + Fibonacci(n-2) 
  
#calculator functions 
if(op == 0):
    a = int(input("Enter your first input: "))
    b = int(input("Enter your second input: "))
    print(a+b)

elif(op == 1):
    a = int(input("Enter your first input: "))
    b = int(input("Enter your second input: "))
    print(a-b)

elif(op == 2):
    a = int(input("Enter your first input: "))
    b = int(input("Enter your second input: "))
    print(a * b)

elif(op == 3):
    a = int(input("Enter your first input: "))
    b = int(input("Enter your second input: "))
    print(a/b)

elif(op == 4):
    a = int(input("Enter your first input: "))
    b = int(input("Enter your second input: "))
    print(a ** b)

elif(op == 5):
    c = int(input("Enter your first input: "))
    print(math.sqrt(c))

elif(op == 6):
    c = int(input("Enter your first input: "))
    print(math.factorial(c))

elif(op == 7):
    c = int(input("Enter your first input: "))
    print(str(Fibonacci(c))) 






