# Take numbers from a user and show the average of the numbers the user entered.
len=int(input("Enter how many numbers you want to enter: ")) 

nums = []

for i in range(len):
    num = int(input("Enter a number: "))
    nums.append(num)
total = sum(nums)
average = total / len
print("The average of the numbers you entered is: ",round(average,2))
""" multi line commnet 
where we can comment multi line at a time  """

""" hello
dhewo """
#another solution of this one 
length = int(input("Enter how many numbers you want to enter: "))

for i in range(length):
    num = int(input())
    total+=num
avg = total / length
print("The average of this : ",round(avg,2))    