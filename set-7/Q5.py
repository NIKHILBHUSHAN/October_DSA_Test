'''class Solution:
    def findInMountainArray(self,nums,h):
        for i in range(len(nums)):
            if nums[i]==h:
                return i
        return -1
'''
class Solution:
    def findInMountainArray(self,nums,h):
        n=len(nums)
        lo=0
        hi=n-1
        while lo<hi:
            mid=lo+(hi-lo)//2
            if nums[mid]<nums[mid+1]:
                lo=mid+1
            else:
                hi=mid
        peak=lo
        lo=0
        hi=peak
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if nums[mid]==h:
                return mid
            elif nums[mid]<h:
                lo=mid+1
            else:
                hi=mid-1
        lo=peak+1
        hi=n-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if nums[mid]==h:
                return mid
            elif nums[mid]>h:
                lo=mid+1
            else:
                hi=mid-1
        return -1