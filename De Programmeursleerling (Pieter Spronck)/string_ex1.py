text = 'I am the best in the world'

i = 0
while i < len(text):
    if i == 'a' or 'e' or 'i' or 'o' or 'u':
        print(text[i], '- ', end='')
        print(i)
        i += 1
    else:
        continue