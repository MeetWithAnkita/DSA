# Task:
# Find the longest common prefix shared by all strings.
words = ["flower", "flow", "flight"]
if not words:
    print("")
else:
    max_len = min(len(word) for word in words)
    print("Minimum Length: ", max_len)

    store = []
    for i in range(max_len):
        char = words[0][i]
        match = True

        for j in range(1, len(words)):
            if words[j][i] != char:
                match = False
                break
        if match:
            store.append(char)
        else:
            break
    print("Longest Common Prefix: ", ("".join(store)))

        





