class Solution:
    def countPoints(self, rings: str) -> int:
        arr = [""] * 10
        
        for i in range(0,len(rings),2):
            color=rings[i]
            idx=int(rings[i+1])
            if color not in arr[idx]:
                arr[idx] += color
        cnt=0
        for i in arr:
            if len(i) == 3:
                cnt+=1
        return cnt

