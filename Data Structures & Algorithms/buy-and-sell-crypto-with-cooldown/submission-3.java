class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length; 
        int[][] dp = new int[n + 1][2];
        boolean[] buysell = {true, false};

        for (int i = n - 1; i > -1; i--) {
            for (boolean isBuy: buysell) {
                if (isBuy) {
                    int buy = i + 1 < n ? dp[i + 1][1] - prices[i] : -1 * prices[i];
                    int cooldown = i + 1 < n ? dp[i+1][0] : 0;
                    dp[i][0] = Math.max(buy, cooldown);
                } else {
                    int sell = i + 2 < n ? dp[i + 2][0] + prices[i] : prices[i];
                    int cooldown = i + 1 < n ? dp[i+1][1] : 0;
                    dp[i][1] = Math.max(sell, cooldown);
                }
            }
        }

        return dp[0][0];
    }
}
