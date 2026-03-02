class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        idx = 0
        mp={}
        for i in key:
            if i != " " and i not in mp:
                mp[i] = alphabet[idx]
                idx += 1
                if idx >= 26:
                    break
        ans = ""
        for i in message:
            if i != " ":
                ans += mp[i]
            else:
                ans += " "
        return ans
