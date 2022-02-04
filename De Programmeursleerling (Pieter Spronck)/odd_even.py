from pcinput import getInteger

number = getInteger('Please enter a number: ')
result = number % 2

if result == 0:
    print('The number you entered is even!')
else:
    print('The number you entered is odd!')