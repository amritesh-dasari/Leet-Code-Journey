class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        if len(t)==0:
            return False
        countr=0
        for i in t:
            print(s[countr])
            if s[countr]==i:
                countr+=1
                if countr==len(s):
                    return True
        return False