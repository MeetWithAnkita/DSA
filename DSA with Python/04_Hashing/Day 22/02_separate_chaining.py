'''What is Separate Chaining?

When two or more keys get the same hash index, we store all those keys 
in a collection (such as a list) at that index.'''

'''Here is a simplified example of Separate Chaining 
    using a list of lists.'''

size = 7 

table = [[] for _ in range(size)]

def insert(key):
    index = key % size
    table[index].append(key)

keys = [10, 17, 24, 5]

for key in keys:
    insert(key)

print(table)