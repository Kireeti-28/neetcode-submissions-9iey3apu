class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inOrder = {}
        outOrder = {}

        for trustPair in trust:
            a = trustPair[0]
            b = trustPair[1]

            if b not in inOrder:
                inOrder[b] = 0
            
            if a not in outOrder:
                outOrder[a] = 0

            inOrder[b] += 1
            outOrder[a] += 1
        
        for k, v in inOrder.items():
            if v == len(trust) and k not in outOrder:
                return k
        
        return -1