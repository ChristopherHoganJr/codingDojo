# 1 - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countdown(num):
    newList = [num]
    for i in range(num,0,-1):
        newList.append(i-1)
    return newList
a = countdown(5)

# 2 - Create a function that will receive a list with two numbers. Print the first value and return the second.
def print_and_return(lst):
    print(lst[0])
    return lst[1]

# 3 - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def first_plus_length(lst):
    return lst[0] + len(lst)

# 4 - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    newlst = [x for x in lst if x > lst[1]]
    print(len(newlst))
    return newlst

# 5 - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def length_and_value(size, value):
    newlst = []
    for i in range(size):
        newlst.append(value)
    return newlst
