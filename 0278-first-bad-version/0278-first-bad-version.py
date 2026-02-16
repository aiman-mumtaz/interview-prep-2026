# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n==1:
            return n
        i,j=1,n
        ans=0
        while i<=j:
            mid = i + (j-i) // 2
            if isBadVersion(mid):
                ans=mid
                j=mid-1
            else:
                i=mid+1
        return ans
