text = 'I am the best in the world'
vowels = 'aeiou'

i = 0

while i < len(text):
        if text[i] in vowels:
                print(text[i], '-', i)
        i += 1
