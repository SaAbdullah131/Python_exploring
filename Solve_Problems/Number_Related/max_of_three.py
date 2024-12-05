#Find the largest of the three numbers.
num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))
num3=int(input("Enter another number: "))
if num1>num2:
    if num1>num3:
        max_num=num1
elif num2>num3:
    if num2>num1:
        max_num=num2
else:
    max_num=num3
print(max_num)            

#shortcut of this one
num11=int(input("Enter a number: "))
num22=int(input("Enter another number: "))
num33=int(input("Enter another number: "))
largest = max(num11,num22,num33)
print(largest)