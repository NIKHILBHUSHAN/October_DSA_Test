'''class Solution:
    def searchInsert(self,nums,t):
        for i in range(len(nums)):
            if nums[i]>=t:
                return i
        return len(nums)
'''
class Solution:
    def searchInsert(self,nums,t):
        lo=0
        hi=len(nums)
        while lo<hi:
            mid=lo+(hi-lo)//2
            if nums[mid]<t:
                lo=mid+1
            else:
                hi=mid
        return lo