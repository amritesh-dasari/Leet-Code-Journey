def romanToInt(s: str) -> int:
    sum=0
    for i in range(len(s)):
        
        if s[i]=='I':
            sum+=1
        elif s[i]=='V':
            sum+=5
        elif s[i]=='X':
            sum+=10
        elif s[i]=='L':
            sum+=50
        elif s[i]=='C':
            sum+=100
        elif s[i]=='D':
            sum+=500
        elif s[i]=='M':
            sum+=1000
        
        if i!=0:
            if s[i]=='V':
                if s[i-1]=='I':
                    sum-=2
            elif s[i]=='X':
                if s[i-1]=='I':
                    sum-=2
            elif s[i]=='L':
                if s[i-1]=='X':
                    sum-=20
            elif s[i]=='C':
                if s[i-1]=='X':
                    sum-=20
            elif s[i]=='D':
                if s[i-1]=='C':
                    sum-=200
            elif s[i]=='M':
                if s[i-1]=='C':
                    sum-=200
    return sum