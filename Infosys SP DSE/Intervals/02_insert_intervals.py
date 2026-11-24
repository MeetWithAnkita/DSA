'''
Insert Interval
You are given a list of non-overlapping intervals sorted 
by their starting time.

You are also given a new interval.

Insert the new interval into the list and merge any 
overlapping intervals.
'''

# intervals = [[1,3], [6,9]]
# newInterval = [2,5]

intervals = [[1,2], [3,5], [6,7], [8,10], [12,16]]
newInterval = [4,9]

def inserted_interval(intervals, newInterval):
    res = []
    i = 0 
    n = len(intervals) #5

    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1 

    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1 

    res.append(newInterval)
    while i < n:
        res.append(intervals[i])
        i += 1

    return res

print(inserted_interval(intervals, newInterval))