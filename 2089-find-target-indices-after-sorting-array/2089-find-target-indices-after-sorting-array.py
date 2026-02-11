class Solution:
    def targetIndices(self, a: List[int], k: int) -> List[int]:
        a.sort()
        ans = []
        for i, val in enumerate(a):
            if val == k:
                ans.append(i)
        return ans