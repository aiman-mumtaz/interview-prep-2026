class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        h_mp = {i: 0 for i in range(1,len(nums)+1)}
        for x in nums:
            h_mp[x] = h_mp.get(x, 0) + 1
        
        for key in h_mp:
            print(key, h_mp[key])

        return [i for i,x in h_mp.items() if x == 0]