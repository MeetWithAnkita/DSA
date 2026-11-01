size = 11
keys = [22, 33, 44, 55, 66]

def quadratic_probing(keys, size):
    table = [None] * size

    def index(key):
        for i in range(size):
            j = ( key % size + pow(i, 2)) % size
            if table[j] == None:
                table[j] = key
                break

    for k in keys:
        index(k)

    return table


print(quadratic_probing(keys, size))


'''Complexity
- Best-case insertion: O(1)
- Worst-case insertion: O(size)
- Building the table: O(n × size) worst case.
- Space: O(size).'''