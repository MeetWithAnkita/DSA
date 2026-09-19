s = "programming"

freq = {}
for i in s:
   freq[i] = freq.get(i, 0) + 1
max = 0

for i in freq:
   if max < freq[i]:
      max = freq[i]

for i in freq:
    if freq[i] == max:
        print(i)
print(freq)
