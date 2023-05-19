def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    if sum(gas)>=sum(cost):
        for i in range(len(gas)):
            gasstations=[]
            for j in range(i+1,len(cost)):
                gasstations.append(j)
            for j in range(i+1):
                gasstations.append(j)
            gasincar=0
            gasincar+=gas[i]
            print(f"Initial Station {i}: {gasincar}")
            print(f"Cost to station {i}: {cost[i]}")
            gasincar-=cost[i]
            for k in gasstations:
                print(f"Station {k}: {gasincar}")
                if gasincar<0:
                    print("Tank Empty")
                    break
                if k==gasstations[-1]:
                    print(f"LAST STATION GET  {k}")
                    return k
                gasincar+=gas[k]
                gasincar-=cost[k]
    return -1