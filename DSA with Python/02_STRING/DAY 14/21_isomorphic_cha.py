# What does “Isomorphic” mean?

# Two strings are isomorphic if we can replace each distinct character
# in the first string with a corresponding character in the second string,
# while preserving the character pattern.

# Rules:

# Each character must always map to the same character.
# Two different characters cannot map to the same character.
# Both strings must have the same length.


s = "egg"
t = "add"

if len(s) != len(t):
    print("False")
else:
    s_to_t = {}
    t_to_s = {}
    isomorphic = True

    for i in range(len(s)):
        ch1 = s[i]
        ch2 = t[i]

        if ch1 in s_to_t:
            if s_to_t[ch1] != ch2:
                isomorphic = False
                break

        elif ch2 in t_to_s:
            isomorphic = False
            break

        else:
            s_to_t[ch1] = ch2
            t_to_s[ch2] = ch1

    print(isomorphic)