from pcinput import getInteger

total = 0
count = 0

while count < 5:
    if count == 0:
        total += getInteger('Please enter the first number: ')
        count += 1
    if count == 1:
        total += getInteger('Please enter the second number: ')
        count += 1
    if count == 2:
        total += getInteger('Please enter the third number: ')
        count += 1
    if count == 3:
        total += getInteger('Please enter the fourth number: ')
        count += 1
    if count == 4:
        total += getInteger('Please enter the final number: ')
        count += 1

avg = total/count

print ('Total is', total)
print('Average of the number is', avg)