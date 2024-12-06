startNumber = int(input("Enter a number where start :  "))
endNumber = int(input("Enter number where to end: "))

odd= 0
while startNumber <= endNumber:
    if(startNumber%2!=0):
        print(startNumber)
        odd+=1
    startNumber+=1

print(f"There are {odd} odd numbers in the range {startNumber} to {endNumber}")
