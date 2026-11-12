class Solution:
    def majorityElement(self,nums:list[int])->int:
        """for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    count+=1
            if count>len(nums)//2:
                return nums[i]"""
        candidate=None
        count=0
        for num in nums:
            if count==0:
                candidate=num
            if num==candidate:
                count+=1
            else:
                count-=1
        return candidate