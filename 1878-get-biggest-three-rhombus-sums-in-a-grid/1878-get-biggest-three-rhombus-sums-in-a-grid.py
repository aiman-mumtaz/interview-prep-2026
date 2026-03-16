class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sums = set()

        for i in range(m):
            for j in range(n):
                sums.add(grid[i][j])
                
                r = 1
                while i - r >= 0 and i + r < m and j - r >= 0 and j + r < n:
                    current_sum = 0
                    
                    for k in range(r):
                        current_sum += grid[i - r + k][j + k]
                    for k in range(r):
                        current_sum += grid[i + k][j + r - k]
                    for k in range(r):
                        current_sum += grid[i + r - k][j - k]
                    for k in range(r):
                        current_sum += grid[i - k][j - r + k]
                    
                    sums.add(current_sum)
                    r += 1
        
        return sorted(list(sums), reverse=True)[:3]