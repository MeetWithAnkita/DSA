arr = [1, 3, 4,3, 2, 2]
#  Find duplicate using BRUTE FORCE
position = 0
print("Duplicate: ")
while position < (len(arr) - 1):
    for i in range(position + 1, len(arr)):
        if arr[position] == arr[i]:
            print(arr[position])
    position += 1