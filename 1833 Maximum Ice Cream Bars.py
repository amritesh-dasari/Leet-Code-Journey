def maxIceCream(costs: list[int], coins: int) -> int:
    costs.sort()
    num=0
    add=0
    for i in costs:
        if add+i<=coins:
            num+=1
            add+=i
        else:
            break
    return num

costs=[1,3,2,4,1]
coins=7
res=maxIceCream(costs, coins)
print(res)