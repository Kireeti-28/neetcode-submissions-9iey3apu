class Solution {
    public int helper(int i, int[] prices, boolean isBuying, Map<String, Integer> visited) {
        if (i >= prices.length)
        return 0;

        String curState = String.valueOf(i) + String.valueOf(isBuying);
        if (visited.containsKey(curState)) return visited.get(curState);

        if (isBuying) {
            int buy = helper(i + 1, prices, !isBuying, visited) - prices[i];
            int cooldown = helper(i + 1, prices, isBuying, visited);
            visited.put(curState, Math.max(buy, cooldown));
        } else {
            int sell = helper(i + 2, prices, !isBuying, visited) + prices[i];
            int cooldown = helper(i + 1, prices, isBuying, visited);
            visited.put(curState, Math.max(sell, cooldown));
        }

        return visited.get(curState);
    }

    public int maxProfit(int[] prices) {
        return helper(0, prices, true, new HashMap());
    }
}
