num = int(input('Please input a number: '))
table = range(1, 11)
count = 1

while count <11:
    print(count, '*', num, '=', (count*num))
    count += 1