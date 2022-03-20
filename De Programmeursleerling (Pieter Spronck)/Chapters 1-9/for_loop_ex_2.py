from pcinput import getInteger

total = 0

for x in range(5):
    number = getInteger('Please input a number: ')
    total += number

print(total)
print('Done')
