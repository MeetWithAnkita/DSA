size = 5
keys = [12, 7, 22, 9, 14]


def separate_chaining(size, keys):
    table = [[] for _ in range(size)]
    def index(key):
        i = key % size
        table[i].append(key)
    for i in keys:
        index(i)
    return table 

print(separate_chaining(size, keys))


'''Complexity analysis
- Insertion: O(1) average per key (assuming good distribution).
- Building the complete table: O(n) average.
- Space: O(m + n), where m is table size and n is number of keys.'''