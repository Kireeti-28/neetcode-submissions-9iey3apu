class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            want = target - nums[i]

            if want in mp:
                return [mp[want], i]
            
            mp[nums[i]] = i
        
        return [-1. -1]