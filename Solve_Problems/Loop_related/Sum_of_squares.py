#Sum of squares 
""" Take a number as input. Then get the sum of the numbers. If the number is n. Then get """
def square_sum(num):
    sum=0
    for i in range(num+1):
        sqaure = (i**2)
        sum+=sqaure
    return sum

num = int(input("Enter a number: "))
square = square_sum(num)
print("The sum of the squares of the numbers from 1 to",num,"is",square)

""" Another way to some this problem in following """
def sum_of_square2(n):
    sum = n*(n+1)*(2*n+1)/6
    return sum

num = int(input('Enter a number: '))
sum = sum_of_square2(num)
print('Your sum of Square is: ', sum)

#f string 
name = "SA Abdullah"
age = 26
print(f"My Name is {name} and I am {age} years old" )