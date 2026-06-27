class Solution {
    public int helper(int i, int[] prices, boolean isBuying) {
        if (i >= prices.length)
        return 0;

        if (isBuying) {
            int buy = helper(i + 1, prices, !isBuying) - prices[i];
            int cooldown = helper(i + 1, prices, isBuying);
            return Math.max(buy, cooldown);
        } else {
            int sell = helper(i + 2, prices, !isBuying) + prices[i];
            int cooldown = helper(i + 1, prices, isBuying);
            return Math.max(sell, cooldown);
        }
    }

    public int maxProfit(int[] prices) {
        return helper(0, prices, true);
    }
}
