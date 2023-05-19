def numJewelsInStones(J: str, S: str) -> int:
    jewelCount = 0
    for char in S:
        if char in J:
            jewelCount += 1
    return jewelCount