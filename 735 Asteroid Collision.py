class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        temp=[]
        for i in asteroids:
            if not temp or i>0:
                temp.append(i)
            else:
                while True:
                    peek=temp[-1]
                    if peek<0:
                        temp.append(i)
                        break
                    elif peek == -i:
                        temp.pop()
                        break
                    elif peek>-i:
                        break
                    else:
                        temp.pop()
                        if not temp:
                            temp.append(i)
                            break
        return temp