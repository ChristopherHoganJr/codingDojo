# print('hey there!')

## defining a variable
# hello_string = 'hey it\'s me!'
## python version of console.log
# print(hello_string)

# def say_phrase(name):
#     if len(name) >= 20:
#         print(f'Greetings from a faraway land, fine sir/madam/knighted honorable {name}')
#     elif len(name) > 10:
#         print(f'Salutations, fine {name}')
#     else:
#         print(f'hello, {name}')

# say_phrase('Christopher')

# Arrays
# nums = [4,8,15,16,23,42]
# print(nums[2])

## Dictionaries
# sundae = {
#     'flavor': 'vanilla',
#     'sauce': 'raspberry syrup',
#     'scoops': 10,
#     'toppings': ['peanuts', 'chocolate shavings', 'whipped cream', 'cherry'],
# }

# print(sundae['toppings'])

## Loops
# count = 0
# while(count < 10):
#     print(count)
#     count += 1



## For N Loop
# nums = [ 4,6,8,10,12,14]
# for num in nums:
#     num *= 2
#     print(num)

# print(nums)

## For Range Loop = for i in range(start,end,step)
# for num in range(1, -101, -5):
#     print(num)

### Javascript
# for(var i = 0; i < 100; i++) {
#   block body
# }

### Python
# for i in range(100):
#     block body

# -------------------------------------------------------------------

## Basic 13
# Print all integer form 1 to 255
# for i in range(255):
#     print(i+1)

# 2
def printSum(maxInt):
    total = 0
    for i in range(maxInt+1):
        total += i
        print(f'i: {i} - total: {total}')
    return total
# Print Sum 0 - 255
# printSum(255)

# 3 Given an array, find and print its largest element
def largestElement(arr):
    largest = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            print(f'Found a new largest: {largest}')
    print(f'Largest number in array is: {largest}')
    return largest
# largestElement([1,2,3,1000,2,-18,8000,9,4,67,0])

# 4 Array with odds between 1 and 255
def oddInts():
    newArr = [x for x in range(1,256) if x % 2 != 0]
    print(newArr)
    return newArr

# oddInts()

# 5 Shift Array Values
def shiftArr(arr):
    for i in range(len(arr)):
        if i < len(arr) - 1:
            arr[i] = arr[i+1]
        else:
            arr[i] = 0
    print(arr)

shiftArr([1,2,3,4,5,6])