class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        
        def dfs(i, n):
            if i >= n:
                return 0
            
            if i in memo:
                return memo[i]

            step_one = dfs(i + 1, n)
            step_two = dfs(i + 2, n)

            memo[i] = min(step_one, step_two) + cost[i]
            return memo[i]
        
        return min(dfs(0, len(cost)), dfs(1, len(cost)))