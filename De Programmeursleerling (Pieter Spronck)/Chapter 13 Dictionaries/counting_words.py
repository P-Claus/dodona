
def word_count(s):
    s_lower = s.lower()
    s_strip = s_lower.strip('?,.')
    s_split = s_strip.split()
    dict = {}  
    for word in s_split:
        if word in dict:
            dict[word] += 1 
        else:
            dict[word] = 1
    return dict
