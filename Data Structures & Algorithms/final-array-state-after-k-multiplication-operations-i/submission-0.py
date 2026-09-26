class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            min_num = min(nums)
            idx = nums.index(min_num)
            nums[idx] *= multiplier
        
        return nums