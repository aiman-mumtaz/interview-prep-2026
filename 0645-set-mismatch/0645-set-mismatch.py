class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        h_mp = {i: 0 for i in range(1,len(nums)+1)}
        for x in nums:
            h_mp[x] = h_mp.get(x, 0) + 1
        duplicate,missing=-1,-1
        for i in range(1, len(nums)+ 1):
            if h_mp[i] == 2:
                duplicate = i
            elif h_mp[i] == 0:
                missing = i
                
        return [duplicate, missing]