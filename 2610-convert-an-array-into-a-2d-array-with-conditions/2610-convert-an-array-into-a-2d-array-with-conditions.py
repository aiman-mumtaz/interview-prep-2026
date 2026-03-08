from collections import Counter

class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        res = []
        counts = Counter()
        
        for num in nums:
            # How many times have we seen this number before?
            row_idx = counts[num]
            
            # If the current frequency requires a new row, add one
            if row_idx >= len(res):
                res.append([])
            
            # Place the number in the corresponding row
            res[row_idx].append(num)
            
            # Increment frequency for next time we see this number
            counts[num] += 1
            
        return res