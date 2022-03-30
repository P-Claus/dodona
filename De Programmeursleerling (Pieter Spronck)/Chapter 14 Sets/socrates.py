things = {'Socrates', 'Plato', 'Eratosthenes', 'Zeus', 'Hera', 'Athens', 'Acropolis', 'Cat', 'Dog'}
men = {'Socrates', 'Plato', 'Eratosthenes'}
mortals = {'Socrates', 'Plato', 'Eratosthenes', 'Cat', 'Dog'}



A = men.issubset(mortals)

B = 'Socrates' in men


C = 'Socrates' in mortals

D = things.intersection(mortals) not in men


E = mortals.issuperset(men)
