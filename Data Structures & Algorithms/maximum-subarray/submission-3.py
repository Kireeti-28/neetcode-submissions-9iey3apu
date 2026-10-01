class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = 0

        for num in nums:
            cur_sum += num
            if cur_sum < 0:
                cur_sum = 0
            
            max_sum = max(cur_sum, max_sum)
        
        if max_sum == 0:
            return min(nums)
        return max_sum