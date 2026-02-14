class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mxCnt=0
        tmpCnt=0
        for i in nums:
            if i == 1:
                tmpCnt += 1
                mxCnt = max(mxCnt,tmpCnt)
            else:
                tmpCnt=0
        return mxCnt
