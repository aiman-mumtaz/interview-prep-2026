class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        prefix_diff = [[0] * (cols + 1) for _ in range(rows + 1)]
        prefix_x = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        res = 0
        
        for r in range(rows):
            for c in range(cols):
                val_diff = 0
                val_x = 0
                
                if grid[r][c] == 'X':
                    val_diff = 1
                    val_x = 1
                elif grid[r][c] == 'Y':
                    val_diff = -1
                
                prefix_diff[r+1][c+1] = (val_diff + prefix_diff[r][c+1] + 
                                         prefix_diff[r+1][c] - prefix_diff[r][c])
                
                prefix_x[r+1][c+1] = (val_x + prefix_x[r][c+1] + 
                                      prefix_x[r+1][c] - prefix_x[r][c])
                
                if prefix_diff[r+1][c+1] == 0 and prefix_x[r+1][c+1] > 0:
                    res += 1
                    
        return res