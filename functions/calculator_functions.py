""" Write four functions: add(a, b), subtract(a, b), multiply(a, b), divide(a, b).
 Each returns the result. Build a simple menu to call them."""

def add(a,b): 
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b ==0 :
        return "can't divide by 0"
    else:
        return a/b

print("--Avaiable Operations--")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Choose operation: "))
if choice not in  [1,2,3,4]:
    print("Invalid")
    exit()

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))


if choice == 1:
    print(add(a,b))
elif choice == 2:
    print(subtract(a,b))
elif choice == 3:
    print(multiply(a,b))
elif choice == 4:
    print(divide(a,b))


