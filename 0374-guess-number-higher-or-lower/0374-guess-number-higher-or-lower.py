# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        i=1
        while i<=n:
            mid = i + (n-i) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) > 0:
                i=mid+1
            else:
                n=mid-1
        return n