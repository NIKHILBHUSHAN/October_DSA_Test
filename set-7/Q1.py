'''class Solution:
    def search(self,nums,q):
        for i in range(len(nums)):
            if nums[i]==q:
                return i
        return -1
'''
class Solution:
    def search(self,nums,q):
        lo=0
        hi=len(nums)-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if nums[mid]==q:
                return mid
            elif nums[mid]<q:
                lo=mid+1
            else:
                hi=mid-1
        return -1