class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n= len(nums)
        eS= n*(n+1) // 2
        aS=0
        for i in nums:
            aS += i
        return eS-aS
