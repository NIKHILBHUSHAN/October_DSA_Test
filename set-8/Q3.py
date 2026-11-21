'''class Solution:
    def findMin(self,nums):
        smallest=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<smallest:
                smallest=nums[i]
        return smallest
'''
class Solution:
    def findMin(self,nums):
        lo=0
        hi=len(nums)-1
        while lo<hi:
            mid=lo+(hi-lo)//2
            if nums[mid]>nums[hi]:
                lo=mid+1
            else:
                hi=mid
        return nums[lo]