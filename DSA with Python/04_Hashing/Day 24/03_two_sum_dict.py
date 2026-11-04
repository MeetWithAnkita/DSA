nums = [2, 7, 3, 11, 15, 6]
target = 9

# store = {}
# for i in range(len(nums)):
#     com = target - nums[i]
#     if com in store:
#         print(store[com], i)
#     else:
#         store[nums[i]] = i

def two_sum(arr, target):
    store = {}
    '''
    for i, num in enumerate(arr):
        complement = target - num
    '''
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in store:
            return (store[complement], i)
        else:
            store[arr[i]] = i

print(two_sum(nums, target))