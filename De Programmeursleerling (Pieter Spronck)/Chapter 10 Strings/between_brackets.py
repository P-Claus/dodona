text = input('Please enter a sentence: ')
x = 0
bracket = '['
bracket1 = ']'
new_word = ''

while x < len(text):
    left_bracket = text.index('[')
    right_bracket = text.index(']')
    subs = text[left_bracket:right_bracket]
    print(subs)
    new_word += subs

    x += 1

print(new_word)





    #if text[x] == bracket:
        #]
        #new_word += text[x:bracket1]
    #x += 1

#clean_wrd = new_word.replace('[', '')
#clean_wrd2 = clean_wrd.replace(']', '')

#print(clean_wrd2.strip())