class Solution:
    def getFloorCeil(self,nums,q):
        '''
        floor=None
        ceil=None
        for x in nums:
            if x<=q:
                floor=x
            if x>=q and ceil==None:
                ceil=x
        return [floor,ceil]
        '''
        n=len(nums)
        l=0
        r=n-1
        floor=None
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]<=q:
                floor=nums[mid]
                l=mid+1
            else:
                r=mid-1
        l=0
        r=n-1
        ceil=None
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]>=q:
                ceil=nums[mid]
                r=mid-1
            else:
                l=mid+1
        return [floor,ceil]