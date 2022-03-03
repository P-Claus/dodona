num = int(input('Please input a number: '))
num_loop = num
dividers = 0

loop = range(num_loop)

for i in loop:
    #print(num_loop)
    if num % num_loop == 0:
        dividers += 1
    num_loop -= 1

if dividers >= 3:
    print(num, 'is not a prime')
else:
    print(num, 'is a prime')