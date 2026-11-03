'''
Your task: Create a new list containing only distinct 
elements while preserving their original order.
'''

arr = [4, 2, 4, 3, 2, 5, 3, 6]
seen = set()
l = []
for i in (arr):
    if i not in seen:
        seen.add(i)
        l.append(i)

print(l)