'''
Given an array containing numbers from 1 to n, 
one number is missing and another number appears twice.
'''

nums = [1, 2, 2, 4, 5]

def find_missing_repeated_ele(nums):
    seen = set()
    repeat = set()
    n = len(nums)
    total = 0

    for i in nums:
        if i not in seen:
            seen.add(i)
            total += i
        else:
            repeat.add(i)
    missing = ((n * (n + 1)) // 2 ) - total

    return (next(iter(repeat)), missing)


repeat, missing = (find_missing_repeated_ele(nums))
print("Missing: ", missing)
print("Repeated: ", repeat)

# iter() creates an iterator from an iterable (like a set, list, or tuple).
# It returns an iterator object.
# next() retrieves the next element from an iterator.