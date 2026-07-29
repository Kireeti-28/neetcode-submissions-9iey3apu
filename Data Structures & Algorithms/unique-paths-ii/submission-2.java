class Solution {
    private int helper(int i, int j, int[][] obstacleGrid) {
        if (i >= obstacleGrid.length || j >= obstacleGrid[i].length)
            return 0;

        if (obstacleGrid[i][j] == 1)
            return 0;

        if (i == obstacleGrid.length - 1 && j == obstacleGrid[i].length - 1)
            return 1;

        return helper(i, j + 1, obstacleGrid) + helper(i + 1, j, obstacleGrid);
    }
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        return helper(0, 0, obstacleGrid);
    }
}