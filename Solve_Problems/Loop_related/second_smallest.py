#For a list, find the second smallest element in the list
def second_smallest(list):
    smallest = list[0]
    second_smallest= list[0]
    for i in range(1,len(list)):
        if list[i]<smallest:
            second_smallest = smallest
            smallest = list[i]
            
        elif list[i]<second_smallest:
            second_smallest =list[i]
        return second_smallest


numbers = [44,11,83,29,25,76,88]
second_smallest = second_smallest(numbers)
print("Second smallest number is : ", second_smallest)
