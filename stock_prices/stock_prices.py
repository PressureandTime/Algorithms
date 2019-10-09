# #!/usr/bin/python

import argparse


def find_max_profit(prices):
  index_of_smallest = 0
  index_of_biggest = 0

  elements = len(prices)
  for i in range(elements):
    if prices[i] < prices[index_of_smallest]:
      index_of_smallest = i
    elif prices[i] > prices[index_of_biggest]:
      index_of_biggest = i





if __name__ == "__main__":
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description="Find max profit from prices.")
    parser.add_argument(
        "integers", metavar="N", type=int, nargs="+", help="an integer price"
    )
    args = parser.parse_args()

    print(
        "A profit of ${profit} can be made from the stock prices {prices}.".format(
            profit=find_max_profit(args.integers), prices=args.integers
        )
    )


# **** ? this version is not working, find out why

# def getMaxProfit(arr):
#   minIdx = 0
#   maxIdx = 1
#   currMin = 0
#   maxProfit = 0


#   elements = len(arr)
#   i = 1
#   for i in range(elements):
#     if (arr[i] < arr[currMin]):
#       currMin = i

#   if (arr[maxIdx] - arr[minIdx] < arr[i] - arr[currMin]):
#     maxIdx = i
#     minIdx = currMin

#   maxProfit = arr[maxIdx] - arr[minIdx]
#   return maxProfit


# arr1 = [1050, 270, 1540, 3800, 2]
# arr2 = [1]
# print(getMaxProfit(arr1))


#*************************

# Returns maximum profit with two transactions on a given
# list of stock prices price[0..n-1]
def maxProfit(price,n):

    # Create profit array and initialize it as 0
    profit = [0]*n

    # Get the maximum profit with only one transaction
    # allowed. After this loop, profit[i] contains maximum
    # profit from price[i..n-1] using at most one trans.
    max_price=price[n-1]

    for i in range(n-2, 0 ,-1):

        if price[i]> max_price:
            max_price = price[i]

        # we can get profit[i] by taking maximum of:
        # a) previous maximum, i.e., profit[i+1]
        # b) profit by buying at price[i] and selling at
        #    max_price
        profit[i] = max(profit[i+1], max_price - price[i])

    # Get the maximum profit with two transactions allowed
    # After this loop, profit[n-1] contains the result
    min_price=price[0]

    for i in range(1,n):

        if price[i] < min_price:
            min_price = price[i]

        # Maximum profit is maximum of:
        # a) previous maximum, i.e., profit[i-1]
        # b) (Buy, Sell) at (min_price, A[i]) and add
        #    profit of other trans. stored in profit[i]
        profit[i] = max(profit[i-1], profit[i]+(price[i]-min_price))

    result = profit[n-1]

    return result


price = [1050, 270, 1540, 3800, 2]
print ("Maximum profit is", maxProfit(price, len(price)))
