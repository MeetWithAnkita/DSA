arr = [7, 9, 11, 1, 3, 5]
# arr = [ 11, 1, 3 ,5, 7, 9]

def find_minimum(arr):
    s = 0
    e = len(arr) - 1 
    while s < e:
        m = ( s+e ) // 2 
        # if arr[m] < arr[e]:
        #     e = m 
        if arr[m] > arr[e]:
            s = m + 1 
        else:
            e = m
    return arr[s]


print(find_minimum(arr))