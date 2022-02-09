nums = [-2,1,-3,4,-1,2,1,-5,4]
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         for i in range(1, len(nums)):
#             if nums[i-1] > 0:
#                 nums[i] += nums[i-1]
#         return max(nums)

# Best soln 2
from itertools import accumulate
x = max(accumulate(nums, lambda x, y: x+y if x > 0 else y))


# sol 3
# for i in range(1,len(nums)):
#     nums[i] = max(nums[i], nums[i-1] + nums[i])
#     print(nums)