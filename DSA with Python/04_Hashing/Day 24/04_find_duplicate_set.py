nums = [1, 2, 3, 2, 4, 5, 1, 6, 3]

def find_duplicate(arr):
    seen = set()
    duplicate = set()
    for i in arr:
        if i in duplicate:
            continue 
        elif i in seen:
            duplicate.add(i)
        elif i not in seen:
            seen.add(i)
    return duplicate

print(find_duplicate(nums))