nums = [1,3,4,2,2]

t = h = nums[0]
while True:
    t = nums[t]
    h = nums[nums[h]]
    if t == h:
        break
    # cycle found
# Find the "entrance" to the cycle.
t = nums[0]
while t != h:
    t = nums[t]
    h = nums[h]

print(h)