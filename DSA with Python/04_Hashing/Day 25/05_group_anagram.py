# Problem: Given a list of strings, group together all 
# strings that are anagrams of each other.

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

def group_anagram(words):
    store = {}

    for w in words:
        s_w = ''.join(sorted(w)) #list to str
        if s_w in store:
            store[s_w].append(w)
        else:
            store[s_w] = [w]
    return list(store.values())

print(group_anagram(words))

'''
Operation	            Complexity
Sorting one word	    O(k log k)
Processing all words	O(n × k log k)
Dictionary operations	O(1) average per operation
Overall time	        O(n × k log k)
Space	                O(n × k)
'''