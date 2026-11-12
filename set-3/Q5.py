class Solution:
    def removeDuplicates(self,nums:list[int])->int:
        """result=[]
        count=0
        previous=None
        for num in nums:
            if num!=previous:
                count=1
                previous=num
                result.append(num)
            elif count<2:
                count+=1
                result.append(num)
        for i in range(len(result)):
            nums[i]=result[i]
        return len(result)"""
        if len(nums)<=2:
            return len(nums)
        position=2
        for i in range(2,len(nums)):
            if nums[i]!=nums[position-2]:
                nums[position]=nums[i]
                position+=1
        return position