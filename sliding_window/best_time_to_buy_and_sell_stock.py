'''
You are given an integer array, prices, where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:

Input: prices = [10,8,7,5,2]

Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:

1 <= prices.length <= 100
0 <= prices[i] <= 100
'''

# My Solution (Did not work)

'''
Error 1: Should have been, current_price - lowest_price (Line 50)
Error 2: Returned ther wrong value, should have been biggest_profit (Line 55)
Error 3: biggest_profit should have been initialized to 0. (Line 40)

'''

def maxProfit(self, prices: List[int]) -> int:

    lowest_price = prices[0]
    biggest_profit = float('-inf')

    for i in range(1, len(prices)):

        current_price = prices[i]

        if current_price < lowest_price:
            lowest_price = current_price
        
        else:
            profit = lowest_price - current_price

            if biggest_profit < profit:
                biggest_profit = profit
    
    return profit

# Fixed Solution
def maxProfit(self, prices: List[int]) -> int:
    lowest_price = prices[0]
    biggest_profit = 0

    for i in range(1, len(prices)):
        current_price = prices[i]

        if current_price < lowest_price:
            lowest_price = current_price
        else:
            profit = current_price - lowest_price
            if profit > biggest_profit:
                biggest_profit = profit
    
    return biggest_profit

# NeetCode Solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP