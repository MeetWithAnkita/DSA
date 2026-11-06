s = "leetcode"

def first_unique_cha(s):
    freq = {}
    for i in s:
        freq[i] = freq.get(i, 0) + 1 
    for i in s:
        if freq[i] == 1:
            return i

print(first_unique_cha(s))