class Solution {
    public int minDays(int[][] grid) {

        // 섬을 찾는다.
        if (checkIsland(grid) != 1) return 0;

        for (int r = 0; r < grid.length; r++){
            for (int c = 0; c < grid[0].length; c++) {
                if (grid[r][c] == 1) {
                    grid[r][c] = 0;
                    if (checkIsland(grid) != 1) return 1;
                    grid[r][c] = 1;
                }
            }
        }


        return 2;
    }
    private int checkIsland(int[][] grid) {
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        int islands = 0;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                if (grid[r][c] == 1 && !visited[r][c]) {
                   islands++;
                   dfs(grid, r, c, visited); 
                }
            }
        }
        return islands;
    }

    private void dfs(int[][] grid, int r, int c, boolean[][] visited) {
        visited[r][c] = true;
        int[] dr = {1, -1, 0, 0};
        int[] dc = {0, 0, -1, 1};
        for (int idx = 0; idx < 4; idx++) {
            int nr = r + dr[idx];
            int nc = c + dc[idx];
            if (nr < 0 || nr >= grid.length || nc < 0 || nc >= grid[0].length || visited[nr][nc] || grid[nr][nc] == 0) continue;
            dfs(grid, nr, nc, visited);
        }
    }

}