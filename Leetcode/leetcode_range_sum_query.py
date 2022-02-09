class NumArray(object):
    def __init__(self, nums):
        self.dp = nums
        for i in range(1, len(nums)):
            self.dp[i] += self.dp[i-1]

    def sumRange(self, i, j):
        return self.dp[j] - (self.dp[i-1] if i > 0 else 0)
### calculate sumsumRange(lo, hi), we sum up the numbers and return the result. So the time complexity would be O(n). 
# Note that there are many calls to sumRange function, so we can calculate the prefix sum in the constructor. 
# Then each time we call the sumRange(lo, hi), we just need to calculate the prefix[hi] - prefix[lo - 1], in O(1) time. 
 


# nums = [-2,0,3,-5,2,-1]
# nums = [0,1,2,3]
# dp = nums[:]
# for i in range(1, len(nums)):
#     dp[i] += dp[i-1]
#     print(dp)

# i = 3
# j = 1
# x = dp[j] - (dp[i-1] if i > 0 else 0)
# print(x)