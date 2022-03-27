from pcinput import getInteger

amount = getInteger('What is the weigth of your suitcase?')

if amount > 20:
    print('There is a $$25 surcharge for luggage that is too heavy.')
elif amount < 20:
    print('Have a safe flight!')
elif amount == 20:
    print('Pfew! The weight is just right!')