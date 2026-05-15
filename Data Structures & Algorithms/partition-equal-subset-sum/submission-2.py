class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 == 1:
            return False
        
        memo = {}
        def dfs(i, cur_sum, target):
            if (cur_sum == target):
                return True

            if i >= len(nums) or cur_sum > target:
                return False
            
            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]

            pick = dfs(i + 1, cur_sum + nums[i], target)
            nopick = dfs(i + 1, cur_sum, target)

            memo[(i, cur_sum)] = pick or nopick
            return memo[(i, cur_sum)]
        
        return dfs(0, 0, totalSum // 2)