class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_area = 0
        
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
        
        for i in range(m):
            current_row = sorted(matrix[i], reverse=True)
            
            for j in range(n):
                height = current_row[j]
                width = j + 1
                max_area = max(max_area, height * width)
                
        return max_area