# s1 = "listen"
# s2 = "silent"

s1 = "hello"
s2 = "world"

def check_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    freq = {}
    for i in s1:
        freq[i] = freq.get(i, 0) + 1 
    for i in s2:
        if i in freq:
            freq[i] -= 1 
            if freq[i] == 0 :
                del freq[i]
        else:
            return False
    if freq:
        return False 
    else:
        return True

print(check_anagram(s1, s2))
print(check_anagram("listen", "silent"))