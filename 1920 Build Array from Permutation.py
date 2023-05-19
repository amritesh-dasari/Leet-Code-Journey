def buildArray(nums: list[int]) -> list[int]:
    temp=[]
    for i in range(len(nums)):
        temp.append(nums[nums[i]])
    return temp

nums=[0,2,1,5,3,4]
res=buildArray(nums)
print(res)