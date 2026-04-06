class Solution {
    private class GridItem {
        private int x;
        private int y;

        public GridItem(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() {
            return this.x;
        }

        public int getY() {
            return this.y;
        }
    }

    // public void bfs(int r, int c, int[][] grid, boolean[][] visited) {
    //     Queue<Pair> queue  = new LinkedList<>();

    //     queue.offer(new Pair(r, c));

    //     while (queue.size() > 0) {
    //         Pair curPair = queue.poll();
    //         int curX = curPair.getX();
    //         int curY = curPair.getY();

    //     }
    // }

    public int dfs(int i, int j, int[][] grid, boolean[][] visited) {
        if (i >= grid.length || i < 0 || j >= grid[0].length || j < 0 
            || grid[i][j] == 0) {
            return 1;
        }

        if (visited[i][j]) {
            return 0;
        }

        visited[i][j] = true;

        int right = dfs(i, j + 1, grid, visited);
        int left = dfs(i, j - 1, grid, visited);
        int up = dfs(i + 1, j, grid, visited);
        int down = dfs(i - 1, j, grid, visited);


        return right + left + up + down;
    }

    public int islandPerimeter(int[][] grid) {
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[r].length; c++) {
                visited[r][c] = false;
            }
        }

        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[r].length; c++) {
                if (grid[r][c] == 1) {
                    return dfs(r, c, grid, visited);
                }
            }
        }

        return dfs(0, 0, grid, visited);
    }
}