nums = [2, 7, 3, 11, 15, 6]
target = 9

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])


'''
Complexity:
- Time: O(n²)
- Space: O(1)
'''