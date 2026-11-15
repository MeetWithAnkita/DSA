'''
Capacity To Ship Packages Within D Days (LeetCode 1011).

A ship must transport all packages within 5 days.

Rules:
- Packages must be shipped in the given order.
- The ship has a maximum weight capacity.
- Each day, load as many consecutive packages as possible 
    without exceeding the capacity.

    
Our goal is to find the minimum ship capacity that can 
deliver all packages within 5 days.


'''
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5

def check_possible_capasity(weights, days, capacity):
    total_load = 0 
    day = 1

    for w in weights:
        total_load += w
        if total_load > capacity:
            day += 1
            total_load = w
        
    return day <= days


def min_ship_capacity(weights, days):
    left = max(weights)
    right = sum(weights)

    while left <= right:
        mid = left + (right - left) // 2 
        if check_possible_capasity(weights, days, mid):
            ans = mid 
            right = mid - 1 
        else:
            left = mid + 1
    return ans 

print(min_ship_capacity(weights, days))

'''
For Capacity To Ship Packages Within D Days:
- Minimum capacity = max(weights) = 10
- Maximum capacity = sum(weights) = 55
'''

'''
Complexity analysis
Let n be the number of packages and S be their total weight.
- Feasibility function: O(n)
- Binary search: O(log S)
- Overall time: O(n * log S)
- Auxiliary space: O(1)
'''