class Solution {
    public int helper(int i, int[] prices, int isBuying, int[][] visited) {
        if (i >= prices.length)
        return 0;

        if (visited[i][isBuying] != -1) return visited[i][isBuying];

        if (isBuying == 1) {
            int buy = helper(i + 1, prices, 0, visited) - prices[i];
            int cooldown = helper(i + 1, prices, 1, visited);
            visited[i][isBuying] = Math.max(buy, cooldown);
        } else {
            int sell = helper(i + 2, prices, 1, visited) + prices[i];
            int cooldown = helper(i + 1, prices, 0, visited);
            visited[i][isBuying] = Math.max(sell, cooldown);
        }

        return visited[i][isBuying];
    }

    public int maxProfit(int[] prices) {
        int[][] visited = new int[prices.length][2];
        
        for (int i = 0 ; i < prices.length; i++) {
            Arrays.fill(visited[i], -1);
        }

        return helper(0, prices, 1, visited);
    }
}
