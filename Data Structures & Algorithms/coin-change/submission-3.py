class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = float('inf')

        def dfs(i, current_amount, cur_coins):
            nonlocal min_coins
            if i >= len(coins) or current_amount > amount:
                return
            
            if current_amount == amount:
                min_coins = min(min_coins, cur_coins)
                return
            
            cur_coins += 1
            dfs(i, current_amount + coins[i], cur_coins)
            cur_coins -= 1
            dfs(i + 1, current_amount, cur_coins)
        
        dfs(0, 0, 0)
        return -1 if min_coins == float('inf') else min_coins
        



