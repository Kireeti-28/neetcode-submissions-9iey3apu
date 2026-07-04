class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            hold = dp[i + 1]
            for j in range(2):
                if j == 0:
                    # buy
                    buy = dp[i + 1][1] - prices[i]
                    dp[i][j] = max(hold[j], buy)
                else:
                    # sell
                    sell = dp[i + 1][0] + prices[i]
                    dp[i][j] = max(hold[j], sell)

        print(dp)
        return dp[0][0]