class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            
            mat = self.rotate(mat)
            
        return False

    def rotate(self, matrix: list[list[int]]) -> list[list[int]]:
        return [list(row[::-1]) for row in zip(*matrix)]