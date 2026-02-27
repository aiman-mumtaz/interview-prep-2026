class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedArr = sorted(nums)
        mp={}
        for i, num in enumerate(sortedArr):
            if num not in mp:
                mp[num] = i
        return [mp[num] for num in nums]      