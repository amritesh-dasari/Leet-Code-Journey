class Solution:
    def reverseVowels(self, s: str) -> str:
        vowellist=[]
        for i in s:
            if i.lower() in ["a","e","i","o","u"]:
                vowellist.append(i)
        temp=""
        for i in range(len(s)):
            if s[i].lower() in ["a","e","i","o","u"]:
                temp+=vowellist.pop()
            else:
                temp+=s[i]
        return temp