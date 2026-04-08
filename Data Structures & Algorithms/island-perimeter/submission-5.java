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

        public boolean equals(Object obj) {
            if (this == obj) return true;

            if (obj == null || getClass() != obj.getClass()) return false;

            GridItem obj1 = (GridItem) obj;

            return obj1.getX() == this.getX() && obj1.getY() == this.getY();
        }

        public int hashCode() {
            return Objects.hash(this.getX(), this.getY());
        }
    }

    public int bfs(int r, int c, int[][] grid, Set<GridItem> visited) {
        int ROWS = grid.length;
        int COLS = grid[0].length;
        int perimeter = 0;

        Queue<GridItem> queue = new LinkedList<GridItem>();
        List<GridItem> directions = List.of(new GridItem(0, 1), new GridItem(0, -1), new GridItem(1, 0), new GridItem(-1, 0));

        var gridItem = new GridItem(r, c);
        queue.offer(gridItem);
        visited.add(gridItem);

        while (queue.size() > 0) {
            var curGridItem = queue.poll();

            for (GridItem direction: directions) {
                int curRow = curGridItem.getX() + direction.getX();
                int curCol = curGridItem.getY() + direction.getY();
                if (curRow < 0 || curRow >= ROWS || curCol < 0 || curCol >= COLS || grid[curRow][curCol] == 0) {
                    perimeter++;
                } else if (!visited.contains(new GridItem(curRow, curCol))) {
                    queue.offer(new GridItem(curRow, curCol));
                    visited.add(new GridItem(curRow, curCol));
                }
            }
        }

        return perimeter;
    }

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
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[r].length; c++) {
                if (grid[r][c] == 1) {
                    return bfs(r, c, grid, new HashSet<GridItem>());
                }
            }
        }

        return -1;
    }
}