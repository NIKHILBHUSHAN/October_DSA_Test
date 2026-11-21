'''class Solution:
    def firstBadVersion(self,nums):
        for i in range(len(nums)):
            if nums[i]==1:
                return i+1
        return -1
'''
class Solution:
    def firstBadVersion(self,nums):
        lo=0
        hi=len(nums)-1
        ans=-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if nums[mid]==1:
                ans=mid+1
                hi=mid-1
            else:
                lo=mid+1
        return ans