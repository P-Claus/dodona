text1 = input('Please write some words: ')
text2 = input('Please write some words: ')
common_letters = ''

for letter in text2:
    if letter in text1:
        if letter in common_letters:
            continue
        else:
            common_letters += letter


print(common_letters)