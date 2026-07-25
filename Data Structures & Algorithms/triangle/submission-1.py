class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        def recursive(i, j):
            if i >= len(triangle) or j >= len(triangle[i]):
                return 0

            one = triangle[i][j] + recursive(i + 1, j)
            two = triangle[i][j] +recursive(i + 1, j + 1)

            return min(one, two)


        minn = float('inf')
        for i in range(len(triangle[0])):
            minn = min(recursive(i, 0), minn)
        
        return minn