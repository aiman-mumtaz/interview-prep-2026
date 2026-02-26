class Solution:
    def maxDistinct(self, s: str) -> int:
        unique = set("".join(s))
        return len(unique)