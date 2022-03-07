def multiplication_table(number):
    loop = range(10)
    count = 1
    for i in loop:
        total = count * number
        print(count, '*', number, '=', total)
        count += 1
    return

multiplication_table(12)

