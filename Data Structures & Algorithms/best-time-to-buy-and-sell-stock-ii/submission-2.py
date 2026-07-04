class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}

        def dfs(i, choice):
            if (i == len(prices)):
                return 0

            if (i, choice) in memo:
                return memo[(i, choice)]
            '''
            Buy(0) -> profit -= prices[i]

            Sell(1) -> profit += prices[i]
                 -> profit = profit
            '''

            holdProfit = dfs(i + 1, choice)
            if (choice == 0): 
                # buy
                buyProfit = dfs(i + 1, 1) - prices[i]
                memo[(i, choice)] = max(buyProfit, holdProfit)
                return memo[(i, choice)]
            else:
                # sell
                sellProfit = dfs(i + 1, 0) + prices[i]
                memo[(i, choice)] = max(holdProfit, sellProfit)
                return memo[(i, choice)]
                
        return dfs(0, 0)