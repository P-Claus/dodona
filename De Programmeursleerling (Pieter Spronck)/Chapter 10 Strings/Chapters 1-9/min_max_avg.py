#input
a = int(input('Please enter a number: '))
b = int(input('Please enter a number: '))
c = int(input('Please enter a number: '))

#formula
max = max(a, b, c)
min = min(a, b, c)
avg = (a + b+ c) /3

print('maximum:', max)
print('minimum:', min)
print('average: {:.2f}'.format(avg))
