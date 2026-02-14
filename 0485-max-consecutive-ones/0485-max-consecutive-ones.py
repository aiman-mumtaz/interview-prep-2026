class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mxCnt=0
        tmpCnt=0
        for i in nums:
            if i == 0:
                mxCnt = max(mxCnt,tmpCnt)
                tmpCnt=0
            else:
                tmpCnt += 1
        return max(tmpCnt,mxCnt)
