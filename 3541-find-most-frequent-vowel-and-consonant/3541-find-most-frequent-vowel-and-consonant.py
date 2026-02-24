class Solution:
    def maxFreqSum(self, s: str) -> int:
        mp={}
        for i in s:
            mp[i] = mp.get(i,0)+1
        vC,cC=0,0
        for key,value in mp.items():
            if key in ('a','e','i','o', 'u'):
                vC=max(vC,value)
            else:
                cC=max(cC,value)
        return cC+vC