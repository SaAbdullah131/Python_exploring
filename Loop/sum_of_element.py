#For a given list, get the sum of each number in the list
def sum_of_element(list):
    sum =0
    for i in list:
        sum+=i
    return sum 

numbers = int(input('How many numbers you want to enter: '))
list = []
for i in range(numbers):
    num =int(input())
    list.append(num)
result = sum_of_element(list)
print("The sun of element is: ",result)    