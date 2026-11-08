arr = [1, 1, 2, 2, 3, 3, 4]

def remove_duplicate(arr):
    slow = 0 
    for fast in range(1, len(arr)):
        if arr[slow] != arr[fast]:
            slow += 1 
            arr[slow] = arr[fast]
    return (arr[:slow+1])
  

print(remove_duplicate(arr))