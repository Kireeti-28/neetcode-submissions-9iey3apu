class Solution {
    public int bfs(int r, int c, boolean[][] visited, int[][] grid) {
        int ROWS = grid.length;
        int COLS = grid[0].length;
        int area = 1;
        
        Queue<int[]> queue = new LinkedList();
        queue.offer(new int[]{r, c});
        visited[r][c] = true;
        int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        while (!queue.isEmpty()) {
            int[] gridItem = queue.poll();
            int gridItemRow = gridItem[0];
            int gridItemCol = gridItem[1];

            for (int[] direction: directions) {
                int directionRow = direction[0];
                int directionCol = direction[1];

                int curGridDirectionRow = gridItemRow + directionRow;
                int curGridDirectionCol = gridItemCol + directionCol;

                if (curGridDirectionRow < 0 || curGridDirectionRow >= ROWS || curGridDirectionCol < 0 || curGridDirectionCol >= COLS
                    || grid[curGridDirectionRow][curGridDirectionCol] == 0) {
                    continue;
                } else if (visited[curGridDirectionRow][curGridDirectionCol] == false) {
                    queue.offer(new int[]{curGridDirectionRow, curGridDirectionCol});
                    visited[curGridDirectionRow][curGridDirectionCol] = true;
                    area++;
                }
            }
        }

        return area;
    }
    public int maxAreaOfIsland(int[][] grid) {
        int ROWS = grid.length;
        int COLS = grid[0].length;

        boolean[][] visited = new boolean[ROWS][COLS];
        int maxArea = 0;

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (visited[r][c] == false && grid[r][c] == 1) {
                    maxArea = Math.max(maxArea, bfs(r, c, visited, grid));
                }
            }
        }

        return maxArea;
    }
}
