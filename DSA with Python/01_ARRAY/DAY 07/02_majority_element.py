# arr = [2, 2, 1, 1, 1, 2, 2]
# TasK: Find the element that appears more than n/2 times.

# /////////////////// 1st way///////////////////////////////
# print(len(arr)/2) --> float 3.5
# print(len(arr)//2) -> int 3

# freq= {} #dict

# for i in arr:
#     if i in freq:
#         freq[i] += 1 
#     else:
#         freq[i] = 1 
# for i in freq:
#     if freq[i] > float(len(arr)/2):
#         print(i)

# Part	            Your answer	    Result
# Pattern	        Hashing	        ✅
# Data sturacture	Dictionary	    ✅
# Time	            O(n) average	✅
# Space	            O(n)	        ✅

# /////////////////// 2nd Way /////////////////////
# optimal solution: ---->   Pattern: Boyer–Moore Voting Algorithm✅✅✅✅✅✅

arr = [2, 2, 1, 1, 1, 2, 2]
# arr = [1, 2, 3, 4]

candidate = None
count = 0

for i in arr:
    if count == 0:
        candidate = i
    if i == candidate:
        count += 1 
    else:
        count -= 1 
# verify the candidate frequency 
freq = 0 
# frequency 
frequency = 0

for i in arr:
    if i == candidate:
        frequency += 1

if frequency > len(arr)// 2:
    print("Majority:", candidate)
else:
    print("No majority element")

# Hashing       → O(n) time, O(n) space
# Boyer-Moore   → O(n) time, O(1) space ⭐



