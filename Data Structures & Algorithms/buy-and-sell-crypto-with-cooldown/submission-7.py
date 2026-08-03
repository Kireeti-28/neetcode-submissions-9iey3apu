class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def dfs(i, choice):
            if i >= len(prices):
                return 0

            if (i, choice) in memo:
                return memo[(i, choice)]

            res = 0
            if choice == 'B':
                buy = dfs(i + 1, 'S') - prices[i]
                cooldown = dfs(i + 1, 'B')
                res = max(buy, cooldown)
            else:
                sell = dfs(i + 2, 'B') + prices[i]
                cooldown = dfs(i + 1, 'S')
                res = max(sell, cooldown)
        
            memo[(i, choice)] = res
            return memo[(i, choice)]
        
        memo = {}
        return dfs(0, 'B')