class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = {}
        i=1
        for n in nums:
            if n in seen:
                return n
            seen[n] = True
        return 0