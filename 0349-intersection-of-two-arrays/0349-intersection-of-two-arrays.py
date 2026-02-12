class Solution:
    def intersection(self, a1: List[int], a2: List[int]) -> List[int]:
        s1=set(a1)
        s2=set(a2)
        return [i for i in s1 if i in s2]