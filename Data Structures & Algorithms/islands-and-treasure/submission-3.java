class Solution {
    private void bfs(int r, int c, int[][] grid, boolean[][] visited) {
        Queue<int[]> queue = new ArrayDeque<>();
        int[] root = {r, c, 0};
        queue.offer(root);
        visited[r][c] = true;

        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();

            int cr = cur[0];
            int cc = cur[1];
            int dist = 1 + cur[2];

            for (int[] direction: directions) {
                int cdr = cr + direction[0];
                int cdc = cc + direction[1];

                if (cdr < 0 || cdr >= grid.length || cdc < 0 || cdc >= grid[cdr].length || grid[cdr][cdc] == -1 || grid[cdr][cdc] == 0) {
                    continue;
                }

                if (visited[cdr][cdc]) continue;

                grid[cdr][cdc] = Math.min(grid[cdr][cdc], dist);
                visited[cdr][cdc] = true;
                int[] next = {cdr, cdc, dist};
                queue.offer(next);
            }
        }
    }
    public void islandsAndTreasure(int[][] grid) {

        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[r].length; c++) {
                if (grid[r][c] == 0) {
                    boolean[][] visited = new boolean[grid.length][grid[0].length];

                    bfs(r, c, grid, visited);
                }
            }
        }
    }
}
