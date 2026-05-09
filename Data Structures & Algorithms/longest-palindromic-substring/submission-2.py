class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            u = i
            v = i

            while (u >= 0 and v < len(s) and s[u] == s[v]):
                if (v - u + 1 > resLen):
                    resLen = v - u + 1
                    res = s[u: v + 1]
                u -= 1
                v += 1

            x = i
            y = i + 1
            while (x >= 0 and y < len(s) and s[x] == s[y]):
                if (y - x + 1 > resLen):
                    resLen = y - x + 1
                    res = s[x: y + 1]
                x -= 1
                y += 1
        
        return res
            


            