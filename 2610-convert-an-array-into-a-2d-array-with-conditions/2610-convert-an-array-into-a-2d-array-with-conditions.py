from collections import Counter

class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        res = []
        counts = Counter()
        
        for num in nums:
            row_idx = counts[num]
            if row_idx >= len(res):
                res.append([])
            res[row_idx].append(num)
            counts[num] += 1
            
        return res