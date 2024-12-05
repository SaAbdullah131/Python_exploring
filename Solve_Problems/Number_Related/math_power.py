#Take two numbers from the users. Calculate the result of second number power of the first number.
num = int(input("Enter a nummber: "))
power = int(input("Enter a power: "))
result  = num ** power
print("The result is: ", result)

#another solution of this one
base_number = int(input("Enter a number: "))
power_number = int(input("Enter a power:  "))
result = pow(base_number,power_number)
print("The result is: ", result)