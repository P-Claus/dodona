text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood? He would chuck, he would, as much as he could, and chuck as much as a woodchuck would If a woodchuck could chuck wood.'
s = text.lower()
ss = s.strip()
sss = ss.split()
dict = {}

for word in sss:
    if word in dict:
        dict[word] += 1 
    else:
        dict[word] = 1

print(dict)
    

