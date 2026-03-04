from collections import Counter

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count1 = Counter()
        for x in nums1:
            if x % k == 0:
                count1[x // k] += 1
        
        if not count1:
            return 0
            
        count2 = Counter(nums2)
        
        max_val1 = max(count1.keys())
        total_pairs = 0
        
        for v2, freq2 in count2.items():
            for multiple in range(v2, max_val1 + 1, v2):
                if multiple in count1:
                    total_pairs += count1[multiple] * freq2
                    
        return total_pairs