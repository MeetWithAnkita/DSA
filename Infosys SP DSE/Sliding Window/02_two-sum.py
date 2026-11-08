'''
Task:
You are given a sorted array of integers and a target value.

Find the indices of two numbers whose sum equals the target.

Return their indices using 1-based indexing.
'''

numbers = [2, 7, 11, 15]
target = 9

def two_sum(arr, target):
    # freq = {}
    # for i, v in enumerate(arr):
    #     # i menas index, v = value
    #     need = target - v
    #     if need in freq:
    #         return (freq[need], i+1)
    #     else:
    #         freq[v] = i+14

    left = 0 
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (left+1, right+1)
        elif current_sum > target:
                right -= 1 
        else:
                left += 1
    

print(two_sum(numbers, target))

'''
Two Sum II = LeetCode 167

"Since the array is sorted, I use two pointers, 
one at the beginning and one at the end. I calculate their
sum. If the sum is greater than the target, I move the 
right pointer backward. If it is smaller, I move the left 
pointer forward. This continues until I find the required 
pair."



Complexity:
- Time: O(n)
- Auxiliary space: O(1)
'''