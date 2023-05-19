class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append(" ")
        temp=""
        count=1
        for i in range(len(chars)-1):
            if chars[i]==chars[i+1]:
                count+=1
            else:
                temp+=chars[i]
                if count!=1:
                    temp+=str(count)
                    count=1
        chars.clear()
        for i in temp:
            chars.append(i)