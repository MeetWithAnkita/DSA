'''
3Sum || Medium || LeetCode 15

Given an integer array nums, return all unique triplets 
[nums[i], nums[j], nums[k]] such that:

nums[i]+nums[j]+nums[k]=0
'''
nums = [-1, 0, 1, 2, -1, -4]

def three_sum_total_zero(arr):
    arr = sorted(arr) # -4, -1, -1, 0, 1, 2
    ans = []

    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i-1]:
            continue

        left = i + 1 
        right = len(arr) - 1 
        
        while left < right:
            total =  arr[i] + arr[left] + arr[right]
            if total == 0:
                ans.append([arr[i], arr[left], arr[right]])
                left += 1 
                right -= 1 

                while left < right and arr[left] == arr[left - 1]:
                    left += 1 
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

            elif total > 0:
                right -= 1 
            else:
                left += 1
    return ans
print(three_sum_total_zero(nums))

'''
We use:
- i → fixed pointer.
- left → starts just after i.
- right → starts at the last index.
For every fixed i, we search for two numbers using left 
and right.
'''