class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        
        nums.sort(reverse = True)
        N = len(nums)
        target = sum(nums) // k
        visited = [False] * len(nums)

        def dfs(start, currSum, k):
            if k == 0:
                return True
            
            if currSum == target:
                return dfs(0, 0, k - 1)
            
            for i in range(N):
                if visited[i] or currSum + nums[i] > target:
                    continue
                
                visited[i] = True

                if dfs(start + 1, currSum + nums[i], k):
                    return True

                visited[i] = False
            
            return False
        
        return dfs(0, 0, k)
