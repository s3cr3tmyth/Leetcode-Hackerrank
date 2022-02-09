# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6]

intervals = [[1,3],[2,6],[15,18],[8,10]]

# if len(intervals) == 0:
#     return []
intervals.sort(key = lambda x: x[0])
merged = []
merged.append(intervals[0])
for i in range(1,len(intervals)):
    # if the list of merged intervals is empty 
	# or if the current interval does not overlap with the previous,
	# simply append it.
    a=merged[-1]
    b=intervals[i]
    if b[0]>a[-1]:
        merged.append(b)
    else:
        # otherwise, there is overlap,
		#so we merge the current and previous intervals. 
        merged[-1][-1] = max(a[-1],b[-1])

print(merged)
