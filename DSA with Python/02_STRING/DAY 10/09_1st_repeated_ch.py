s = "programming"

# freq = {}
# for i in s:
#     if i not in freq:
#         freq[i] = 1
        
#     else:
#         print("First Repeated: ", i)
#         break

seen = set()
for i in s:
    if i in seen:
        print("First Repeated: ",i)
        break
    seen.add(i)
    
# Complexity
# Time: O(n) average
# Space: O(k)