class Solution {
    public int numMagicSquaresInside(int[][] grid) {
        // count row, col
        int row = grid.length;
        int col = grid[0].length;
        int result = 0;

        // start 1,1 to row-1, col-1
        for (int r = 1; r < row - 1; r++) {
            for (int c = 1; c < col - 1; c++) {
                result += magic(r, c, grid);
            }
        }
        return result;
    }
    public static int magic(int r, int c, int[][] grid) {
        Set<Integer> visited = new HashSet<Integer>();
        // 세로, 가로, 대각선들의 합이 같다.
        if (grid[r][c] != 5) return 0;
        int lu = grid[r-1][c-1];
        int ld = grid[r+1][c-1];
        int ru = grid[r-1][c+1];
        int rd = grid[r+1][c+1];
        if ((lu%2) != 0 || lu < 1 || lu > 9) return 0;
        if ((ld%2) != 0 || ld < 1 || ld > 9) return 0;
        if ((ru%2) != 0 || ru < 1 || ru > 9) return 0;
        if ((rd%2) != 0 || rd < 1 || rd > 9) return 0;
        System.out.println(lu);
        System.out.println(lu % 2);
        System.out.println(ld);
        System.out.println(ru);
        System.out.println(rd);
        visited.add(grid[r][c]);
        visited.add(grid[r-1][c]);
        visited.add(grid[r+1][c]);
        visited.add(grid[r-1][c-1]);
        visited.add(grid[r+1][c+1]);
        if ((grid[r - 1][c] + grid[r + 1][c] ==
        grid[r][c-1] + grid[r][c+1])  ==
        (grid[r-1][c-1] + grid[r+1][c+1] ==
        grid[r-1][c+1] + grid[r+1][c-1])) {
            if (visited.size() == 5) {
                if ((grid[r-1][c-1] + grid[r][c-1] + grid[r+1][c-1] == 15) && 
                grid[r+1][c-1] + grid[r +1][c] + grid[r+1][c+1] == 15) {
                    return 1;
                }
                
            }
            
        }
        return 0;
    }
}