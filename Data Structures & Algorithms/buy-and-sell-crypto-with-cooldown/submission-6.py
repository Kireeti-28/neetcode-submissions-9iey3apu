class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def dfs(i, choice):
            if i >= len(prices):
                return 0


            if choice == 'B':
                buy = dfs(i + 1, 'S') - prices[i]
                cooldown = dfs(i + 1, 'B')
                return max(buy, cooldown)
            else:
                sell = dfs(i + 2, 'B') + prices[i]
                cooldown = dfs(i + 1, 'S')
                return max(sell, cooldown)
        
        return dfs(0, 'B')