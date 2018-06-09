cost = float(input('Enter the cost: '))
# multiply 18% tip by cost of the meal
tip = 0.18 * cost
# multiply 7% tax by cost of the meal
tax = 0.07 * cost
# add the tip and tax to cost to get the total cost of the meal
total = cost + tip + tax
# display tip amount in $ format
print('tip $', format( tip, ',.2f'))
# display tax amount in $ format
print('tax $', format(tax, ',.2f'))
# display total cost of mean in $ format
print('total $', format(total, ',.2f'))



