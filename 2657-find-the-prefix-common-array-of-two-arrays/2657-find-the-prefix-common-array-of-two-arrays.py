class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)
        res=[0] * n
        freq=[0]*(n + 1)
        cnt = 0
        
        for i in range(n):
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                cnt += 1
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                cnt += 1
            res[i] = cnt
            
        return res