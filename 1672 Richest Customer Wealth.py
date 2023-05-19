def maximumWealth(accounts: list[list[int]]) -> int:
    maxlst=[]
    for i in accounts:
        wealth=0
        for j in i:
            wealth+=j
        maxlst.append(wealth)
    return max(maxlst)