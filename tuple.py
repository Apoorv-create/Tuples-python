month = ("January", "February", "March", "April", "May", "June", "July",
         "August", "September", "October", "November", "December")

profits = (25000, 23800, 12039, 40000, 78900, 11000, 23400, 69400, 75643, 90200, 15607, 86555)

max_profits = max(profits)
max_profits_index = profits.index(max_profits)
print(max_profits_index)

max_profit_month = month[max_profits_index]
print("The maximum profit is " + str(max_profits) + 
      " Was recorded in the month of " + 
      str(max_profit_month))

min_profits = min(profits)
min_profits_index = profits.index(min_profits)
print(min_profits_index)

min_profits_month = month[min_profits_index]
print("The minimum Profits is " + str(min_profits) +
      " Was recorded in the month of " + str(min_profits_month))