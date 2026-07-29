class Solution {
    private int dfs(int i, int j, int[][] grid, int[][] dp) {
        if (i >= grid.length || j >= grid[i].length) return Integer.MAX_VALUE;

        if (dp[i][j] != -1) return dp[i][j];

        if (i == grid.length - 1 && j == grid[i].length - 1) {
            return grid[i][j];
        }

        int right = dfs(i, j + 1, grid, dp);
        int down = dfs(i + 1, j, grid, dp);

        dp[i][j] = grid[i][j] + Math.min(right, down);
        return dp[i][j];
    }

    public int minPathSum(int[][] grid) {
        int r = grid.length;
        int c = grid[0].length;
        int[][] dp = new int[r + 1][c + 1];
        for (int i = 0; i < dp.length; i++) {
            Arrays.fill(dp[i], -1);
        }

        return dfs(0, 0, grid, dp);
    }
}