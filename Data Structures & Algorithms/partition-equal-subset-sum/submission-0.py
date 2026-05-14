class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 == 1:
            return False
        
        def dfs(i, cur_sum, target):
            if i >= len(nums):
                return False
            
            if (cur_sum == target):
                return True

            return dfs(i + 1, cur_sum + nums[i], target) or dfs(i + 1, cur_sum, target)
        
        return dfs(0, 0, totalSum // 2)