class Solution {
    private int dfs(int i, int j, int[][] grid) {
        if (i == grid.length - 1 && j == grid[i].length - 1) {
            return grid[i][j];
        }

        if (i >= grid.length || j >= grid[i].length) return Integer.MAX_VALUE;

        int right = dfs(i, j + 1, grid);
        int down = dfs(i + 1, j, grid);

        return grid[i][j] + Math.min(right, down);
    }

    public int minPathSum(int[][] grid) {
        return dfs(0, 0, grid);
    }
}