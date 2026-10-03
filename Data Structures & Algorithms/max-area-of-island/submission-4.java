class Solution {
    private int dfs(int r, int c, int[][] grid) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[r].length || grid[r][c] == 0) {
            return 0;
        }

        grid[r][c] = 0;

        return 1 + dfs(r, c + 1, grid) + dfs(r, c - 1, grid) + dfs(r + 1, c, grid)
            + dfs(r - 1, c, grid);
    }
    public int maxAreaOfIsland(int[][] grid) {
        int ROWS = grid.length;
        int COLS = grid[0].length;
        int maxArea = 0;

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == 1) {
                    int area = dfs(r, c, grid);
                    maxArea = Math.max(area, maxArea);
                }
            }
        }

        return maxArea;
    }
}
