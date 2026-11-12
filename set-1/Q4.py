class Solution:
    def pivotIndex(self,nums:list[int])->int:
        """for i in range(len(nums)):
            left_sum=0
            right_sum=0
            for j in range(i):
                left_sum+=nums[j]
            for j in range(i+1,len(nums)):
                right_sum+=nums[j]
            if left_sum==right_sum:
                return i
        return -1"""
        total=0
        for num in nums:
            total+=num
        left_sum=0
        for i in range(len(nums)):
            right_sum=total-left_sum-nums[i]
            if left_sum==right_sum:
                return i
            left_sum+=nums[i]
        return -1