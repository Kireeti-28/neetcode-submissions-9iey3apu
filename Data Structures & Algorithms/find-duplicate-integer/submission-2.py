class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mp = {}
        for n in nums:
            if n not in mp:
                mp[n] = 1
            else:
                mp[n] += 1
            
            if mp[n] > 1:
                return n
        
        return -1