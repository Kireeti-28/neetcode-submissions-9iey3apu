class Solution {
    public void islandsAndTreasure(int[][] grid) {
        Queue<int[]> queue = new ArrayDeque<>();

        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[r].length; c++) {
                if (grid[r][c] == 0) {
                    queue.offer(new int[]{r, c, 0});
                }
            }
        }

        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();

            int cr = cur[0];
            int cc = cur[1];
            int dist = cur[2];

            for (int[] direction: directions) {
                int cdr = cr + direction[0];
                int cdc = cc + direction[1];

                if (cdr < 0 || cdr >= grid.length || cdc < 0 || cdc >= grid[cdr].length || grid[cdr][cdc] != Integer.MAX_VALUE) {
                    continue;
                }

                grid[cdr][cdc] = 1 + dist;
                queue.offer(new int[]{cdr, cdc, 1 + dist});
            }
        }
    }
}
