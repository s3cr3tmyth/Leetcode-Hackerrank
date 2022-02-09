tasks = ["A","A","A","B","B","B"]
n = 2
import collections
tasks_count = list(collections.Counter(tasks).values())
max_count = max(tasks_count)
max_count_tasks = tasks_count.count(max_count)
x =  max(len(tasks), (max_count-1)*(n+1)+max_count_tasks)