class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        
        N = len(nums)
        target = sum(nums) // k

        def dfs(start, target):
            if target == 0:
                return 1
            
            if target < 0:
                return 0

            res = 0
            for i in range(start, N):
                if nums[i] <= target:
                    target -= nums[i]
                    res += dfs(i + 1, target)
                    target += nums[i]
        
            return res

        return dfs(0, target) == k