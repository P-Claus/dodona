text = input('Please enter a sentence: ')
x = 0
new_word = ''
bracket = '['

while x < len(text):
    if text[x] == bracket:
        left_bracket = text.find('[', x)
        right_bracket = text.find(']', x)
        new_word += text[left_bracket:right_bracket].strip('[')
        #print(text[left_bracket:right_bracket])
    x += 1

print(new_word)