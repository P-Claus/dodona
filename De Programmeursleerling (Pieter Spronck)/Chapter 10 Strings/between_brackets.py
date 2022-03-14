text = input('Please enter a sentence: ')
x = 0
new_word = ''
bracket = '['

while x < len(text):
    left_bracket = text.index('[', x)
    right_bracket = text.index(']')

    print(text[left_bracket:right_bracket])
    x += 1