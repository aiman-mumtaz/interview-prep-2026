import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        def totalHeightReduced(T):
            total = 0
            for w in workerTimes:
                if T < w: continue
                
                x = int((-1 + math.sqrt(1 + 8 * T / w)) / 2)
                total += x
                if total >= mountainHeight:
                    return True
            return total >= mountainHeight

        low = 1
        high = max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if totalHeightReduced(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans