class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.rec(grid,i,j)
                    count += 1
                    
        return count
    
    def rec(self,grid,i,j):
        if i<0 or j<0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
            return 0
        
        grid[i][j] = '0'
        self.rec(grid, i+1,j) # up
        self.rec(grid, i-1,j) # dowm
        self.rec(grid,i,j+1) # left
        self.rec(grid,i,j-1) # right