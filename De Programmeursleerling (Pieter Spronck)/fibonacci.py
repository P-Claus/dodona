num = int(input('Please input a number: '))

num1 = 0
num2 = 1

total = num1 + num2

while total < num:
    total += num2
    num1 = num2
    num2 = total
    print(total)

