###### Using Bottom Up approach

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float(inf) for i in range(amount + 1)]
        dp[0] = 0
        for i in range(1,amount+1):
            for j in coins:
                if i >= j:
                    dp[i] = min(dp[i], 1 + dp[i - j])                   
                
        return int(dp[amount]) if dp[amount] != float('inf') else -1

# space complexity would be: M ---samount
# time complexity would be : NxM 