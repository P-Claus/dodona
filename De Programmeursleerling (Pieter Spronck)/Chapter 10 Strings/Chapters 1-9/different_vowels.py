sentence = input('Please enter a sentence: ')
count = 0
a = 'a' 
e = 'e' 
i = 'i' 
o = 'o' 
u = 'u' 
A = 'A'
E = 'E'
I = 'I'
O = 'O'
U = 'U'

if a in sentence:
    count += 1
if A in sentence:
    count += 1
if e in sentence:
    count += 1
if E in sentence:
    count += 1
if i in sentence:
    count += 1
if I in sentence:
    count += 1
if o in sentence:
    count += 1
if O in sentence:
    count += 1
if u in sentence:
    count += 1
if U in sentence:
    count += 1

if count > 1:
    print('The sentence contains', count, 'different vowels.')
elif count == 1:
    print('The sentence contains only', count, 'different vowel.')
else:
    print('The sentence contains no vowels.')
