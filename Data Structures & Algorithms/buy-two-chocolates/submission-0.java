class Solution {
    public int buyChoco(int[] prices, int money) {
        Arrays.sort(prices);

        if (prices.length < 2) return money;

        int originalMoney = money;

        for (int i = 0; i < 2; i++) {
            money -= prices[i];
        }

        if (money < 0) return originalMoney;

        return money;
    }
}