'''class Solution:
    def floorSqrt(self,x):
        s=0
        while (s+1)*(s+1)<=x:
            s+=1
        return s
'''
class Solution:
    def floorSqrt(self,x):
        lo=0
        hi=x
        ans=0
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if mid==0 or mid<=x//mid:
                ans=mid
                lo=mid+1
            else:
                hi=mid-1
        return ans