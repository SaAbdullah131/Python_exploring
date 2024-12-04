#For a given list, get the sum of each number in the list
def sum_of_digits(num):
    sum=0
    for i in num:
        sum+=i
    return sum
# creating an empty list
#lst = []

# number of elements as input
# number = int(input("Enter number of elements: "))
 
# # iterating till the range
# for i in  range(0,number):
#     ele = int(input())
#     lst.append(ele)
number = [1,2,3,4,5,6,7,8,9]
result = sum_of_digits(number)
print(result)

#shortcut of this one
number = [1,2,3,4,5,6,7,8,9,10]
result = sum(number)
print(result)

 