class Solution:
    def largestGoodInteger(self, num: str) -> str:
        goodInts = []

        def isAllSame(s):
            return True if len(set(s)) == 1 else False

        for i in range(len(num)):
            for j in range(i, len(num) + 1):
                if (j - i) == 3 and isAllSame(num[i:j]):
                    goodInts.append(num[i:j])

        return max(goodInts) if len(goodInts) > 0 else ""
                    