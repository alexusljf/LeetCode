class Solution {
public int numIslands(char[][] grid) {
        int islands = 0;
        // use 2 for loops to iterate thru the grid, if we find '1' then we search for the adjacent land
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == '1') {
                    islands++;
                }
                islandSearch(grid, i, j);
            }
        }
        return islands;

    }

    public void islandSearch(char[][] grid, int i, int j) {
        // recursively search the size of an island
        // base conditions: outside boundary or is not a 1
        if (i < 0 || i > grid.length - 1 || j < 0 || j > grid[i].length - 1 || grid[i][j] == '0') {
            return;
        } else {
            // we set already searched index to 0, then recursively search the adjacent index for the whole island
            grid[i][j] = '0';
            islandSearch(grid, i + 1, j);
            islandSearch(grid, i, j + 1);
            islandSearch(grid, i - 1, j);
            islandSearch(grid, i, j - 1);
        }
    }
}