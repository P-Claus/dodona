def isEven():
    even = 'is even'
    uneven = 'is uneven'
    num = int(input('Please enter a number: '))
    if num % 2 == 0:
        return num(even)
    else:
        return num(uneven)

print(isEven())