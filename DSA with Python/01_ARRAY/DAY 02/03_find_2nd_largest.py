arr = [10, 45, 23, 67, 12]

# fst = arr[0]
# snd = arr[0]

fst = float('-inf')
snd = float('inf')

for i in arr:
    if i > fst:
        snd = fst
        fst = i 
    elif i > snd:
        snd = i 

print("Second largest element: ", snd)