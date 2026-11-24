'''
Given an array of intervals, merge all overlapping 
intervals and return the non-overlapping intervals.
'''
# intervals = [[1,3], [2,6], [8,10], [15,18]]
intervals = [[6,8], [1,3], [2,4], [9,10], [3,6]]

def return_non_overlapping_array(intervals):
    intervals.sort()
    current = 0
    res = []
    for i in intervals:
        if not res:
            res.append(i)
        else:
            current = i
            if current[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], current[1])
            else:
                res.append(i)
    return res


print(return_non_overlapping_array(intervals))

'''
Operation	            Complexity
Sorting	                O(n log n)
Traversing intervals	O(n)
Overall time	        O(n log n)
Auxiliary space	        O(n) for result
'''