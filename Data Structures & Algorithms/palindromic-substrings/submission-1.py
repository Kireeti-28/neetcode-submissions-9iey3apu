class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        n = len(s)

        for i in range(n):
            u = i
            v = i

            while (u >= 0 and v < n and s[u] == s[v]):
                cnt += 1
                u -= 1
                v += 1
            
            u = i
            v = i + 1

            while (u >= 0 and v < n and s[u] == s[v]):
                cnt += 1
                u -= 1
                v += 1
        
        return cnt
