'''
Minimum Number of Days to Make Bouquets
LeetCode 1482 || Medium || Binary Search on Answer

Problem statement
You are given:
- bloomDay: An array where each element tells us the day 
            a flower blooms.
- m: Number of bouquets we need to make.
- k: Number of adjacent flowers required for each bouquet.

Rules:
1. A flower can be used only after it blooms.
2. Each bouquet requires exactly k adjacent flowers.
3. A flower cannot be used in more than one bouquet.
4. Find the minimum number of days needed to make m bouquets.
'''

bloomDay = [1, 10, 3, 10, 2]
# bloomDay = [1, 10, 3, ]
m = 2
k = 2
def can_make_bouquets(bloomDay, m, k, day ):
    count = 0
    bouquets = 0 
    for i in bloomDay:
        if i <= day:
            count += 1 
            if count == k:
                bouquets += 1
                count = 0
        else:
            count = 0 
    return bouquets >= m

def min_days(bloomDay, m, k):
    left = min(bloomDay) #1
    right = max(bloomDay) #10
    ans = 0

    if m * k > len(bloomDay):
        return -1

    while left <= right:
        mid = left + (right - left) // 2 # 5

        if can_make_bouquets(bloomDay, m, k, mid):
            ans = mid 
            right = mid - 1
        else:
            left = mid + 1
        
    return ans 

print(min_days(bloomDay, m, k))


'''
Complexity	            Result
-----------------------------------
Feasibility function	O(n)
Binary search	        O(log D)
Total time	            O(n log D)
Auxiliary space	        O(1)
'''