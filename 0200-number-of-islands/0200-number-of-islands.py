class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #helper function to dfs and set island cells to '0'
        def dfs(i,j):
            #check out of bounds, or not '1'
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i-1,j)
            dfs(i+1,j)
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands+=1
                    dfs(i,j)
        return islands