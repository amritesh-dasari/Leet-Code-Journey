def longestCommonPrefix(strs: list[str]) -> str:
    minsubslen=len(strs[0])
    for i in strs:
        if minsubslen>len(i):
            minsubslen=len(i)
    
    res=""
    for j in range(minsubslen,0,-1):
        subs=strs[0][0:j]
        for k in range(len(strs)):
            if subs != strs[k][0:j]:
                print(f"{subs} not in {strs[k][0:j]}")
                break
            if k == (len(strs)-1):
                return subs
    return res

strs = ["flower","flawer","flvwer","flower"]
res = longestCommonPrefix(strs)
print(res)