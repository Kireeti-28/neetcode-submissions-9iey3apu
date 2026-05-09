class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dfs(i, nums):
            if i >= len(nums):
                return 0
            
            step_one = nums[i] + dfs(i + 2, nums)
            step_two = dfs(i + 1, nums)

            return max(step_one, step_two)
        
        return max(dfs(1, nums[:-1]), dfs(0, nums[1:]))