# arr1 = [1, 2, 3, 2, 4, 1]
# arr2 = [2, 1, 4, 2, 3, 1]

arr1 = [1, 2, 3]
arr2 = [1, 2, 3, 4]

# Task: 
# Check whether both arrays contain the same elements with the same frequencies.

freq1 = {}
freq2 = {}

for i in arr1:
    if i in freq1:
        freq1[i] += 1 
    else:
        freq1[i] = 1 
for i in arr2:
    if i in freq2:
        freq2[i] += 1 
    else:
        freq2[i] = 1 

# for i in freq1:
#     if i in freq2:
#         if freq1[i] == freq2[i]:
#             print(i, "-->", freq1[i])

same = True

if len(freq1) != len(freq2):
    same = False
else: 
    for i in freq1:
        if i not in freq2:
            same = False
            break

        if freq1[i] != freq2[i]:
            same = False
            break

print("Same frequency:", same)