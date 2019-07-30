def longest_prefix(s):
    n=len(s)

    for res in range(n//2,0,-1):
        prefix=s[0:res]
        suffix=s[n-res:n]

        if(prefix==suffix):
            return res
    return -1

s='xxnihalxx'
print(longest_prefix(s))