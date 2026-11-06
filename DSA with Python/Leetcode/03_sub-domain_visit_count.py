'''
A website domain "discuss.leetcode.com" consists of 
various subdomains. At the top level, we have "com", 
at the next level, we have "leetcode.com" and at the lowest 
level, "discuss.leetcode.com". When we visit a domain like
"discuss.leetcode.com", we will also visit the parent domains
"leetcode.com" and "com" implicitly.
'''

cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

def sub_domain_visit_count(cpdomains):
    freq = {}
    for entry in cpdomains:
        parts = entry.split()   # 900 "google.mail.com"
        count = int(parts[0])   # 900 --> int
        domain = parts[1]       # google.mail.com

        sub_domain = domain.split(".")  #google mail com , len = 3
        for i in range(len(sub_domain)):
            sub = ".".join(sub_domain[i:])
            freq[sub] = freq.get(sub, 0) + count 
            # google.mail.com = 900     c
            # mail.com = 900 + 1 = 901  c
            # com = 900 + 50 + 1= 951   c
            # yahoo.com = 50            c
            # intel.mail.com = 1        c
            # wiki.org = 5              c
            # org = 5                   c

    result = []
    for d, c in freq.items():
        result.append(f"{c} {d}")

    return result

print(sub_domain_visit_count(cpdomains))
