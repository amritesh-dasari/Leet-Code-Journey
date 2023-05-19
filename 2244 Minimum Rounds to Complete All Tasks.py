def minimumRounds(tasks: list[int]) -> int:
    occur={}
    for i in tasks:
        if i in occur.keys():
            occur[i]+=1
        else:
            occur[i]=1
    res=0
    for i in occur.keys():
        if occur[i] == 1:
            return -1
        if occur[i]%3==0:
            res+=occur[i]/3
        else:
            res+=occur[i]//3 +1
    return int(res)

tasks = [69,65,62,64,70,68,69,67,60,65,69,62,65,65,61,66,68,61,65,63,60,66,68,66,67,65,63,65,70,69,70,62,68,70,60,68,65,61,64,65,63,62,62,62,67,62,62,61,66,69]
final=minimumRounds(tasks)
print(final)