class Solution:
    def removeStars(self, s: str) -> str:
        temp=""
        for i in s:
            if i!="*":
                temp+=i
            else:
                temp=temp[:-1]
        return temp
        