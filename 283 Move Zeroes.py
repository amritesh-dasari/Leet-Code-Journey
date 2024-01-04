class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos=0
        for i in range(len(nums)):
            temp=nums[i]
            if temp!=0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos+=1