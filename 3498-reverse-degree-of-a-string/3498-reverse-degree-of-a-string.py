class Solution:
    def reverseDegree(self, s: str) -> int:
        cnt=0
        for i in range(0,len(s)):
            idx = i+1
            revIdx= 26 - (ord(s[i]) - ord('a'))
            cnt += (idx*revIdx)
        return cnt