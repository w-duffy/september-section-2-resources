# Create a function that takes in a list of prices, `prices` and a given value,
# `val`. Using list comprehension, return all of the prices that are greater
# than the given value. If the price is less than the given price, replace it
# with 0. Hint: This can be done in a single line of code.

# Write your function here.
#!!START SILENT
def gas_prices(prices, val):
  return [i if i > val else 0 for i in prices]
#!!END

print(gas_prices([2.55, -1.45, 10.22, 5.78, -5.92, 6.16], 3.99)) #> [0, 0, 10.22, 5.78, 0, 6.16]
print(gas_prices([5.95, 6.62, 2.22, 6.78, 8.92, 7.03], 2.50)) #> [5.95, 6.62, 0, 6.78, 8.92, 7.03]
print(gas_prices([4.55, 4.15, 2.57, 3.78, 2.92, 0.16], 5.00)) #> [0, 0, 0, 0, 0, 0]