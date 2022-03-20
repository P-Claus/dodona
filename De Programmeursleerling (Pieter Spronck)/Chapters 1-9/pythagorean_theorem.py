a = float(input('Please enther the length of a: '))
b = float(input('Please enther the length of b: '))

c = pow(a, 2) + pow(b, 2) 
real_c = pow(c, 0.5)
print('Length of the hypotenuse: {:.3f}'.format(real_c))