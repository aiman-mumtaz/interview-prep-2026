class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mp={}
        ans = -1
        for i in arr:
            mp[i] = mp.get(i,0)+1
        for i in mp:
            if mp[i] == i:
                ans = max(ans,i)
        return ans