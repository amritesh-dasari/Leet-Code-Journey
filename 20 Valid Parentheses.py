def isValid(s: str) -> bool:
    remaing=[]
    last=""
    res=True
    for i in s:
        if i=="(" or i=="{" or i=="[":
            remaing.append(i)
            last=i
        elif i==")" or i=="}" or i=="]":
            if ((last=="(" and i==")") or (last=="{" and i=="}") or (last=="[" and i=="]")):
                remaing.pop()
                if len(remaing)!=0:
                    last=remaing[-1]
                else:
                    last=""
            else:
                res= False
    if remaing!=[]:
        res=False
    return res