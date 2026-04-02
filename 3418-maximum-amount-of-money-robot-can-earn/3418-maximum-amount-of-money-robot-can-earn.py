class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        if not coins or not coins[0]:
            return 0
        
        m, n = len(coins), len(coins[0])
        INF = float('-inf')
        dp = [[[INF] * 3 for _ in range(n)] for _ in range(m)]
        
        if coins[0][0] >= 0:
            dp[0][0][0] = coins[0][0]
        else:
            dp[0][0][0] = coins[0][0]  
            dp[0][0][1] = 0  
        
        for j in range(1, n):
            for k in range(3):
                if coins[0][j] >= 0:
                    if dp[0][j-1][k] != INF:
                        dp[0][j][k] = max(dp[0][j][k], dp[0][j-1][k] + coins[0][j])
                else:
                    if dp[0][j-1][k] != INF:
                        dp[0][j][k] = max(dp[0][j][k], dp[0][j-1][k] + coins[0][j])
                    
                    if k > 0 and dp[0][j-1][k-1] != INF:
                        dp[0][j][k] = max(dp[0][j][k], dp[0][j-1][k-1])
        
        for i in range(1, m):
            for k in range(3):
                if coins[i][0] >= 0:
                    if dp[i-1][0][k] != INF:
                        dp[i][0][k] = max(dp[i][0][k], dp[i-1][0][k] + coins[i][0])
                else:
                    if dp[i-1][0][k] != INF:
                        dp[i][0][k] = max(dp[i][0][k], dp[i-1][0][k] + coins[i][0])
                    
                    if k > 0 and dp[i-1][0][k-1] != INF:
                        dp[i][0][k] = max(dp[i][0][k], dp[i-1][0][k-1])
        
        for i in range(1, m):
            for j in range(1, n):
                for k in range(3):
                    if coins[i][j] >= 0:
                        if dp[i-1][j][k] != INF:
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + coins[i][j])
                            
                        if dp[i][j-1][k] != INF:
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + coins[i][j])
                    else:
                        if dp[i-1][j][k] != INF:
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + coins[i][j])
                        if dp[i][j-1][k] != INF:
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + coins[i][j])
                        
                        if k > 0:
                            if dp[i-1][j][k-1] != INF:
                                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1])
                            if dp[i][j-1][k-1] != INF:
                                dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k-1])
        
        result = max(dp[m-1][n-1][0], dp[m-1][n-1][1], dp[m-1][n-1][2])
        return result