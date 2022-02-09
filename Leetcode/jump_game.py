# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
nums = [2,3,1,1,4]
lastindex = len(nums) -1

# for i in reversed(nums):
for i in range(len(nums) - 1, -1,-1):
# for i in range(len(nums))[::-1]:
    if(i + nums[i] >= lastindex):
        lastindex = i
        
# return lastindex == 0