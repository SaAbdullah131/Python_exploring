# To swap two variables: the value of the first variable will become the value of the second variable. On the # other hand, the value of the second variable will become the value of the first variable.
num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))
temp = num1
num1=num2
num2=temp
#after swaping the value
print("The first number is: ", num1)
print("The second number is: ", num2)

#shortcut of this one
num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))
num1,num2=num2,num1
print("The first number is: ",num1)
print("The second number is: ",num2)

#another solution of this one is 
a = 5
b =7 
a=a+b
b=a-b
a=a-b
print(a,b)
