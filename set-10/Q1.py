class Solution:
    def sortedSquares(self,nums):
        '''
        res=[]
        for x in nums:
            res.append(x*x)
        i=1
        while i<len(res):
            key=res[i]
            j=i-1
            while j>=0 and res[j]>key:
                res[j+1]=res[j]
                j-=1
            res[j+1]=key
            i+=1
        return res
        '''
        n=len(nums)
        res=[0]*n
        i=0
        j=n-1
        k=n-1
        while i<=j:
            a=nums[i]*nums[i]
            b=nums[j]*nums[j]
            if a>b:
                res[k]=a
                i+=1
            else:
                res[k]=b
                j-=1
            k-=1
        return res