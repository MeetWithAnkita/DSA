# size = 7
# keys = [10, 17, 24]

size = 11
keys = [22, 33, 44, 55, 66]

def linear_probing(size, keys):
    table = [None] * size

    def index(key):
        for i in range(size):
            j = (key % size + i) %  size 
            '''
Because it separates two different operations:
1. key % size → Calculate the original hash index.
2. + i → Move forward when a collision occurs.
            '''
            if table[j] == None:
                table[j] = key
                break

    for k in keys:
        index(k)

    return table

print(linear_probing(size, keys))