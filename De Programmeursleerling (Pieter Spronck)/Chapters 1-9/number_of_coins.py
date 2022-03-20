# amount (in cents)
amount = 1156

#amount of dollars
amount_left_after_dollars = amount % 100
amount_of_cents_in_dollars = amount - amount_left_after_dollars
amount_of_dollars = amount_of_cents_in_dollars / 100
#print(amount_left_after_dollars, amount_of_cents_in_dollars, amount_of_dollars)

#amount of quarters
amount_left_after_quarters = amount_left_after_dollars % 25
amount_of_cents_in_quarters = amount_left_after_dollars - amount_left_after_quarters
amount_of_quarters = amount_of_cents_in_quarters / 25
#print(amount_left_after_quarters, amount_of_cents_in_quarters, amount_of_quarters)

#amount of dimes
amount_left_after_dimes = amount_left_after_quarters % 10
amount_of_cents_in_dimes = amount_left_after_quarters - amount_left_after_dimes
amount_of_dimes = amount_of_cents_in_dimes / 10
#print(amount_left_after_dimes, amount_of_cents_in_dimes, amount_of_dimes)

#amount of nickel
amount_left_after_nickels = amount_left_after_dimes % 5
amount_of_cents_in_nickels = amount_left_after_dimes - amount_left_after_nickels
amount_of_nickels = amount_of_cents_in_nickels / 5
#print(amount_left_after_nickels, amount_of_cents_in_nickels, amount_of_nickels)

#amount of pennies
amount_left_after_pennies = amount_left_after_nickels % 1
amount_of_cents_in_pennies = amount_left_after_nickels - amount_left_after_pennies
amount_of_pennies = amount_of_cents_in_pennies / 1
#print(amount_left_after_pennies, amount_of_cents_in_pennies, amount_of_pennies)

#print the final result
print('Dollars:', int(amount_of_dollars))
print('Quarters:', int(amount_of_quarters))
print('Dimes:', int(amount_of_dimes))
print('Nickels:', int(amount_of_nickels))
print('Cents:', int(amount_of_pennies))
