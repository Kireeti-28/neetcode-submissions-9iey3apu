class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}

        def recursive(i, j):
            if i >= len(triangle) or j >= len(triangle[i]):
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]

            one = triangle[i][j] + recursive(i + 1, j)
            two = triangle[i][j] +recursive(i + 1, j + 1)

            memo[(i, j)] = min(one, two)
            return memo[(i, j)]


        minn = float('inf')
        for i in range(len(triangle[0])):
            minn = min(recursive(i, 0), minn)
        
        return minn