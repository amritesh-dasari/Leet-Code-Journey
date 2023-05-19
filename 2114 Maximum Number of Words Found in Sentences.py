def mostWordsFound(sentences: list[str]) -> int:
    max=0
    for i in sentences:
        words=i.split()
        if max<len(words):
            max=len(words)
    return max