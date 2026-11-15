'''
Koko Eating Bananas (LeetCode 875)

Problem statement
Koko loves eating bananas. There are several piles of 
bananas.

You are given:
- piles: An array where each element represents bananas in 
        a pile.
- h: The total number of hours available.
output: 
k: Koko chooses an eating speed k (bananas per hour).


Rules:
1. Each hour, Koko chooses one pile and eats up to k 
bananas.
2. If the pile has fewer than k bananas, she eats the 
entire pile.
3. She cannot eat from another pile during the same hour.
4. Find the minimum eating speed k that allows her to 
finish all bananas within h hours.

'''
piles = [3, 6, 7, 11]
h = 8

def can_finish(piles, h, k):
    total_hours = 0 
    for  p in piles:
        hours = (p + k - 1) // k
        total_hours += hours 
    return total_hours <= h


def min_eating_speed(piles, h):
    left = 1 
    right = max(piles)
    ans = 0

    while left <= right:
        mid = left + (right - left) // 2 

        if can_finish(piles, h, mid):
            ans = mid 
            right = mid - 1
        else:
            left = mid + 1
    return ans

print(min_eating_speed(piles, h))

'''
Component	                Complexity
can_finish()	            O(n)
Binary search iterations	O(log m)
Total time	                O(n log m)
Auxiliary space	            O(1)
'''
