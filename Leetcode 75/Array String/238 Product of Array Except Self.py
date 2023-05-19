class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward=[0]*len(nums)
        backward=[0]*len(nums)
        fprod=1
        bprod=1
        for i in range(len(nums)):
            fprod*=nums[i]
            bprod*=nums[len(nums)-1-i]
            forward[i]=fprod
            backward[len(nums)-1-i]=bprod
        res=[]
        for i in range(len(nums)):
            if i==0:
                res.append(backward[i+1])
            elif i==len(nums)-1:
                res.append(forward[i-1])
            else:
                res.append(forward[i-1]*backward[i+1])
        return res