things = {'Socrates', 'Plato', 'Eratosthenes', 'Zeus', 'Hera', 'Athens', 'Acropolis', 'Cat', 'Dog'}
men = {'Socrates', 'Plato', 'Eratosthenes'}
mortals = {'Socrates', 'Plato', 'Eratosthenes', 'Cat', 'Dog'}



A = men.issubset(mortals)
#B
if 'Socrates' in men:
    print(True)
#C
if 'Socrates' in men and mortals:
    print(True)
#D
D = things.intersection(mortals).isdisjoint(men)


E = mortals.issuperset(men)
