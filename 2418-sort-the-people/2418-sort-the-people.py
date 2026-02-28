class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mp={}
        for i in range(0,len(heights)):
            mp[heights[i]] = names[i]
        names=[]
        for k in sorted(mp.keys(), reverse=True):
            names.append(mp[k])
        return names