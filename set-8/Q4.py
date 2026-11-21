'''class Solution:
    def search(self,nums,t):
        for i in range(len(nums)):
            if nums[i]==t:
                return i
        return -1
'''
class Solution:
    def search(self,nums,t):
        lo=0
        hi=len(nums)-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if nums[mid]==t:
                return mid
            if nums[lo]<=nums[mid]:
                if nums[lo]<=t and t<nums[mid]:
                    hi=mid-1
                else:
                    lo=mid+1
            else:
                if nums[mid]<t and t<=nums[hi]:
                    lo=mid+1
                else:
                    hi=mid-1
        return -1