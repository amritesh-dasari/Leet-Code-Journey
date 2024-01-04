def mergeAlternately(self, word1: str, word2: str) -> str:
    lengthnum=min(len(word1), len(word2))
    if len(word1)==len(word2):
        fl=False
    else:
        fl=True
    finalres=""
    for i in range(lengthnum):
        finalres+=word1[i]
        finalres+=word2[i]
    if fl:
        if len(word1)==lengthnum:
            finalres+=word2[lengthnum:]
        else:
            finalres+=word1[lengthnum:]
    return finalres