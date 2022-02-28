num = int(input('How many bottles of beer? '))

amount = range(num)


for bottle in amount:
    if num > 2:
        print(num, 'bottles of beer on the wall,', num, 'bottles of beer.')
        print('Take one down, pass it around,', (num-1), 'bottles of beer on the wall.')
    if num == 2:
        print(num, 'bottles of beer on the wall,', num, 'bottles of beer.')
        print('Take one down, pass it around,', (num-1), 'bottle of beer on the wall.')
    if num == 1:
        print(num, 'bottle of beer on the wall,', num, 'bottle of beer.')
        print('Take one down, pass it around,', (num-1), 'bottles of beer on the wall.')
    num -= 1