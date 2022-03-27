highest = 656
smallest = 656
triplicates = 0

loop = range(10)

for i in loop:
    number = int(input('Please enter a number: '))
    if number > highest:
        highest = number
    if number < smallest:
        smallest = number
    if number % 3 == 0:
        triplicates += 1

print('largest:', highest)
print('smallest:', smallest)
print('triplicates:', triplicates)