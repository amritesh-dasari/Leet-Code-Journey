def finalValueAfterOperations(operations: list[str]) -> int:
    x=0
    for i in operations:
        if i=="++x" or i=="x++":
            x+=1
        else:
            x-=1
    return x