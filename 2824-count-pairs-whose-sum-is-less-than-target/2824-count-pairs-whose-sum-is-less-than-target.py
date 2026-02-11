class Solution:
    def countPairs(self, a: List[int], k: int) -> int:
        cnt=0
        a.sort()
        l,r=0,len(a)-1
        while l<r:
            if a[l] + a[r] < k:
                cnt += (r-l)
                l += 1
            else:
                r -= 1
        return cnt
        