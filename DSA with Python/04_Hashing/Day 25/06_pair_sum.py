# nums = [2, 7, 4, 5, 3, 6, 8, 1]
# target = 9
nums = [5, 5]
target = 10

def pair_sum(nums, target):
    result = []
    store = set()
    for i in (nums):
        complement = target - i 

        if complement in store:
            result.append((complement, i))
        else:
            store.add(i)

    return result
print(pair_sum(nums, target))

'''
Approach	                    Time	        Space
Your list-based solution	    O(n²)	        O(n)
Optimized set-based solution	O(n) average	O(n)
'''