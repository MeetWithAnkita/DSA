arr = [4, 8, 12, 16, 20]
target = 12

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        

print(linear_search(arr, target))