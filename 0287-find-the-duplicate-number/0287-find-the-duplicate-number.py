class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = {}
        for n in nums:
            if n in seen:
                return n
            seen[n] = True
        print(seen)
        return 0