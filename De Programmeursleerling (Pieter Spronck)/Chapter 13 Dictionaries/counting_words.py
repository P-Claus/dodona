
def word_count(s):
    dict = {}
    x = s.lower()
    n = x.split()

    for wrd in n:
        o = wrd.strip('?,.')
        if o in dict:
            dict[o] += 1 
        else:
            dict[o] = 1
    return dict
