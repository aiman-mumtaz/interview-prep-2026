class Solution:
    def countPairs(self, a: List[int], k: int) -> int:
        cnt=0
        for i in range(0,len(a)):
            for j in range(i+1, len(a)):
                if(a[i]+a[j] < k):
                    cnt+=1
        return cnt
        