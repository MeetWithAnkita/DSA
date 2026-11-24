'''
Problem statement
You are given an array of intervals.

Your task is to find the minimum number of intervals you 
need to remove so that the remaining intervals do not 
overlap.
'''

# intervals = [[1,2], [2,3], [3,4], [1,3]]

'''
Important greedy concept: 
When two intervals overlap, keeping the interval that 
ends earlier generally leaves more room for future intervals.
'''
'''
First understand the algorithm
We will use:
1. Sort intervals by their ending values.
2. Keep the first interval.
3. Check the next interval:
   - If current[0] < previous_end, it overlaps. 
        Increase removal count.
   - Otherwise, keep it and update previous_end.

'''
intervals = [[1,2], [2,3], [3,4], [1,3]]

def non_overlapping_inetrval(intervals):
    intervals.sort(key = lambda x:x[1])

    n = len(intervals)
    count = 0 
    pre_l = intervals[0][1]
       
    for i in range(1, n):
        current = intervals[i]

        if current[0] < pre_l:
            count += 1 
        else:
            pre_l = current[1
                            ]
    return count

print(non_overlapping_inetrval(intervals))