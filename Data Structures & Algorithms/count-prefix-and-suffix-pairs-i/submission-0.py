class Solution:
    def isPrefixAndSuffix(self, str1, str2) -> bool:
        if (len(str1) > len(str2)):
            return False
        
        # print(str1, str2, str2[0: len(str1)], str2[-1 * len(str1)])
        return str2[0: len(str1)] == str1 and str2[-1 * len(str1):]  == str1


    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    ans += 1
        
        return ans
         