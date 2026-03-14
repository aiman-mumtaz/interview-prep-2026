class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        num_options_per_start = 2**(n - 1)
        total = 3 * num_options_per_start
        
        if k > total:
            return ""
        
        k -= 1
        
        choices = ['a', 'b', 'c']
        res = []
        
        first_idx = k // num_options_per_start
        res.append(choices[first_idx])
        
        k %= num_options_per_start
        
        for _ in range(n - 1):
            num_options_per_start //= 2
            
            last_char = res[-1]
            available = [c for c in ['a', 'b', 'c'] if c != last_char]
            
            char_idx = k // num_options_per_start
            res.append(available[char_idx])
            
            k %= num_options_per_start
            
        return "".join(res)