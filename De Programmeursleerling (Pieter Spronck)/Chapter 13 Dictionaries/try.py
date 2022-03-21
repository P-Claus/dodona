text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood? He would chuck, he would, as much as he could, and chuck as much as a woodchuck would If a woodchuck could chuck wood.'
dict = {}
s = text

x = s.lower()
n = x.split()

for wrd in n:
    o = wrd.strip('?,.')
    if o in dict:
        dict[o] += 1 
    else:
        dict[o] = 1

print(dict)

