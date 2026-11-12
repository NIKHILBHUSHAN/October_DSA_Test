class Solution:
    def findDisappearedNumbers(self,nums:list[int])->list[int]:
        """missing=[]
        for i in range(1,len(nums)+1):
            found=False
            for j in range(len(nums)):
                if nums[j]==i:
                    found=True
                    break
            if not found:
                missing.append(i)
        return missing"""
        for i in range(len(nums)):
            index=abs(nums[i])-1
            if nums[index]>0:
                nums[index]=-nums[index]
        missing=[]
        for i in range(len(nums)):
            if nums[i]>0:
                missing.append(i+1)
        return missing