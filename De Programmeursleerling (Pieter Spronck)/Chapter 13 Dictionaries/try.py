movies_dict = {'Monty Python and the Holy Grail': (9, 10, 9.5, 8.5, 3, 7.5, 8), 
"Monty Python's Life of Brian": (10, 10, 0, 9, 1, 8, 7.5, 8, 6, 9), 
"Monty Python's Meaning of Life": (7, 6, 5),
'And Now For Something Completely Different': (6, 5, 6, 6)}

for key in movies_dict.keys():
    for value in movies_dict[key]:
        rating = sum(value)/len(value)
    print(rating)