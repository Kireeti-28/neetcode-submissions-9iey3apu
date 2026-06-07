class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def tabulation():
            n = len(nums)
            dp = [defaultdict(int) for _ in range(n + 1)]
            dp[0][0] = 1

            for i in range(n):
                for total, count in dp[i].items():
                    dp[i + 1][total + nums[i]] += count
                    dp[i + 1][total - nums[i]] += count
            
            return dp[n][target]
        
        return tabulation()

        memo = {}
        def dfs(i, cur_sum):
            if i == len(nums):
                return 1 if cur_sum == target else 0
            
            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]

            memo[(i, cur_sum)] = dfs(i + 1, cur_sum + nums[i]) + dfs(i + 1, cur_sum - nums[i])
            return memo[(i, cur_sum)]
        
        return dfs(0, 0)