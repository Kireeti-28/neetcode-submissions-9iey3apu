class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = {}
        res = 0

        for ss in s:
            if ss in mp:
                mp[ss] += 1
            else:
                mp[ss] = 1
            
            if mp[ss] % 2 == 0:
                res += 2

        for k, v in mp.items():
            if v % 2 == 1:
                res += 1
                break
        
        return res