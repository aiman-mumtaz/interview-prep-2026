class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l,r=1,len(nums)-1
        while(l<r):
            mid = (l+r) // 2
            cnt = 0
            for i in nums:
                if i <= mid:
                    cnt+=1
            if cnt > mid:
                r=mid
            else:
                l=mid+1
        return l