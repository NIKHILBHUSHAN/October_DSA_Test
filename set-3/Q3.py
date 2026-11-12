class Solution:
    def moveZeroes(self,nums:list[int])->None:
        """result=[]
        for num in nums:
            if num!=0:
                result.append(num)
        for num in nums:
            if num==0:
                result.append(0)
        for i in range(len(nums)):
            nums[i]=result[i]"""
        position=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[position]=nums[i]
                position+=1
        while position<len(nums):
            nums[position]=0
            position+=1