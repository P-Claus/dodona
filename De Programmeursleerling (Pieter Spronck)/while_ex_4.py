from pcinput import getInteger

number = getInteger('Enter a number: ')
total = number * (number - 1)
number -= 1

while number > 1:
    total = total * (number - 1) 
    number -= 1

print(total)
