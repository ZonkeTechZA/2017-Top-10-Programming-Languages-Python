#Add function
def add(a,b):
    return a + b

#Subtract Function
def subtract(a,b):
    return a - b

#Multiply Function
def multiply(a,b):
    return a * b

#Divide Function, here we must check for a divide by zero
def divide(a,b):
    if (b != 0):
        return a / b
    else:
        return "Goodbye, World!"

num1 = int(input("Enter your first number: "))

print("Select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
operation = input("Your operation (1/2/3/4): ")

num2 = int(input("Enter your second number: "))

if operation == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif operation == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif operation == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif operation == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid operation choice")
