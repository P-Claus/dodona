from pcinput import getInteger

number = getInteger('Enter a number: ')
result = number - 1
count = 0
total = 0 

while count == number:
    total += (number * result)
    result -= 1
    count += 1

while count != number:
    total *= result
    result -= 1
    count += 1

print(total)
