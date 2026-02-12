class Solution:
    def maximumCount(self, a: List[int]) -> int:
        a=[ x for x in a if x!= 0]
        l,r=0,len(a)-1
        cntPos,cntNeg=0,0
        while l<=r :
            mid= (l+r) // 2
            if a[mid] < 0:
                l=mid+1
            else:
                r=mid-1
        cntNeg = r+1
        cntPos = len(a)-l
        # print(l,r)
        # print(a[l],a[r])
        # print(cntNeg, cntPos)
        return max(r+1,len(a)-l)
            