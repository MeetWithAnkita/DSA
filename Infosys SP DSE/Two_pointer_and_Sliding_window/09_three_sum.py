'''
Given an integer array, return all unique triplets whose sum is zero.
'''
nums = [-1, 0, 1, 2, -1, -4]

# Expected:
# [[-1, -1, 2], [-1, 0, 1]]

def three_sum(arr):
    arr = sorted(arr)
    ans = []

    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue 
        
        left = i + 1 
        right = len(arr) - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total < 0:
                left += 1 
            elif total > 0:
                right -= 1 
            elif total == 0:
                ans.append([arr[i], arr[left], arr[right]])
                left += 1 
                right -= 1 

                while left < right and arr[left] == arr[left -1 ]:
                    left += 1 

                while left < right and arr[right] == arr[right + 1 ]:
                    right -= 1
    return ans

print(three_sum(nums))