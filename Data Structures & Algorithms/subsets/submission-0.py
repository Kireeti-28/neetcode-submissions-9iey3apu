class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subsets = []

        def dfs(i, cur_subset):
            if i >= len(nums):
                subsets.append(cur_subset[:])
                return
            
            cur_subset.append(nums[i])
            dfs(i + 1, cur_subset)
            cur_subset.pop()
            dfs(i + 1, cur_subset)
        
        dfs(0, [])

        return subsets
