s = "I love Python programming"
# freq = {}
w = s.split()
for i in w:
    # freq[i] = freq.get(i, len(i))
    print(i, " -> ", len(i))
    
# ⏱️ Complexity
# Time: O(n)
# Space: O(n) 
# because of split(); your dictionary additionally uses O(k) where k is the number of distinct words.
