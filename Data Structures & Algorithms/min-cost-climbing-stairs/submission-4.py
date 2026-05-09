class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def dfs(i, n):
            if i >= n:
                return 0


            step_one = dfs(i + 1, n)
            step_two = dfs(i + 2, n)

            return min(step_one, step_two) + cost[i]
        
        return min(dfs(0, len(cost)), dfs(1, len(cost)))