class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2)>len(str1):
            str1, str2 = str2, str1
        res=0
        for i in range(len(str2),0,-1):
            if (float(len(str1)/len(str2[:i])).is_integer()) and(float(len(str2)/len(str2[:i])).is_integer()):
                temp1=str2[:i]*(len(str1)//len(str2[:i]))
                temp2=str2[:i]*(len(str2)//len(str2[:i]))
                if temp1==str1 and temp2==str2:
                    res=i
                    break
        return(str2[:res])