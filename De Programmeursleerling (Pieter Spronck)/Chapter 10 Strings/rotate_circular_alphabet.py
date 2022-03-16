num = int(input('Please enter a number: '))
count = 0

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
new_alphabet = ''

while count < len(alphabet):
    new_alphabet += alphabet[num+1]
    count += 1

print(alphabet)
print(new_alphabet)