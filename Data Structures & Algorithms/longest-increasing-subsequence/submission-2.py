class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dfs(i, prev_idx):
            if i >= len(nums):
                return 0
            
            res = dfs(i + 1, prev_idx)

            if prev_idx == -1 or nums[prev_idx] < nums[i]:
                res = max(res, 1 + dfs(i + 1, i))
            
            return res
        
        return dfs(0, -1)
