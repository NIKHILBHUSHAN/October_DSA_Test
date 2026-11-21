'''class Solution:
    def searchRange(self,nums,x):
        first=-1
        last=-1
        for i in range(len(nums)):
            if nums[i]==x:
                if first==-1:
                    first=i
                last=i
        return [first,last]
'''
class Solution:
    def searchRange(self,nums,x):
        first=-1
        last=-1
        lo=0
        hi=len(nums)-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if nums[mid]==x:
                first=mid
                hi=mid-1
            elif nums[mid]<x:
                lo=mid+1
            else:
                hi=mid-1
        if first==-1:
            return [-1,-1]
        lo=first
        hi=len(nums)-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if nums[mid]==x:
                last=mid
                lo=mid+1
            elif nums[mid]<x:
                lo=mid+1
            else:
                hi=mid-1
        return [first,last]