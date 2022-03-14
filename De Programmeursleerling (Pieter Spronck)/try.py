text = 'And no[w] for s[o]methi[n]g completely [d]iff[er]ent.'
x = 0

while x < len(text):
    wrd1 = text.find('[',x)
    wrd2 = text.find(']')
    print(text[wrd1:wrd2])
    x += 1