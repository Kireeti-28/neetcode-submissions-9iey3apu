class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        
        N = len(nums)
        target = sum(nums) // k
        cnt = [0]

        def dfs(start, target):
            if target == 0:
                cnt[0] += 1
                return
            
            if target < 0:
                return

            for i in range(start, N):
                if nums[i] <= target:
                    target -= nums[i]
                    dfs(i + 1, target)
                    target += nums[i]
        
        dfs(0, target)
        return cnt[0] == k