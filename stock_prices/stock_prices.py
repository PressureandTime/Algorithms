#!/usr/bin/python

"""
******** Polya ********
1) Understand the problem
----------------------
What is our input?
• We recieve a list of integers

What are our restrictions?
• We have to buy first before we can sell

What does the function return?
• Maximum profit between a buy and sell as an integer.

How can we define a buy?
• A Buy index is a price that is in an index before the sell, and it can be greater than the sell price.

How can we define a sell?
• A Sell must be after a Buy price, and it can be less than the buy price making a loss.

2) Plan
----
[10, 7, 5, 8, 11, 9]
• We need to keep track of the temp_min as the Buy
• We need to keep track of the temp_max as the Sell
• We need to keep track of the max_profit_so_far which is based on Sell - Buy
• Loop through the list
• If the value in the current index is less than min
      • temp_min = prices[i] - 10, 7, 5, 2
      • temp_max = 0 - reset this value until next iteration of the loop
• Else if the value in the current index is greater than min and greater than the max
      • max = prices[i]
      • max_profit_so_far = temp_max - temp_min
3) Execute the plan
-------------------
"""


import argparse

def find_max_profit(prices):
  temp_min = prices[0]
  temp_max = prices[1]
  max_profit_so_far = temp_max - temp_min

  for price in prices:
    if price < temp_min:
      temp_min = price
      temp_max = 0

    elif price > temp_min and price > temp_max:
      temp_max = price
      max_profit_so_far = temp_max - temp_min
      
  return max_profit_so_far


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
