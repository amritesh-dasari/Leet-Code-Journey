class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        com=max(candies)
        for i in range(len(candies)):
            if (candies[i]+extraCandies>=com):
                candies[i]=True
            else:
                candies[i]=False
        return candies