class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def dfs(i, choice):
            if (i == len(prices)):
                return 0

            '''
            Buy(0) -> profit -= prices[i]

            Sell(1) -> profit += prices[i]
                 -> profit = profit
            '''

            holdProfit = dfs(i + 1, choice)
            if (choice == 0): 
                # buy
                buyProfit = dfs(i + 1, 1) - prices[i]
                return max(buyProfit, holdProfit)
            else:
                # sell
                sellProfit = dfs(i + 1, 0) + prices[i]
                return max(holdProfit, sellProfit)
                
        return dfs(0, 0)