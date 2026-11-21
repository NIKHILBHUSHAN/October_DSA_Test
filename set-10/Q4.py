class Solution:
    def threeSum(self,nums):
        '''
        n=len(nums)
        res=[]
        i=0
        while i<n-2:
            j=i+1
            while j<n-1:
                k=j+1
                while k<n:
                    if nums[i]+nums[j]+nums[k]==0:
                        a=nums[i]
                        b=nums[j]
                        c=nums[k]
                        if a>b:
                            a,b=b,a
                        if b>c:
                            b,c=c,b
                        if a>b:
                            a,b=b,a
                        found=False
                        for triplet in res:
                            if triplet[0]==a and triplet[1]==b and triplet[2]==c:
                                found=True
                                break
                        if not found:
                            res.append([a,b,c])
                    k+=1
                j+=1
            i+=1
        i=1
        while i<len(res):
            key=res[i]
            j=i-1
            while j>=0 and (res[j][0]>key[0] or (res[j][0]==key[0] and res[j][1]>key[1]) or (res[j][0]==key[0] and res[j][1]==key[1] and res[j][2]>key[2])):
                res[j+1]=res[j]
                j-=1
            res[j+1]=key
            i+=1
        if len(res)==0:
            return None
        return res
        '''
        def mergeSort(arr):
            if len(arr)<=1:
                return arr
            mid=len(arr)//2
            left=mergeSort(arr[:mid])
            right=mergeSort(arr[mid:])
            res=[]
            i=0
            j=0
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j+=1
            while i<len(left):
                res.append(left[i])
                i+=1
            while j<len(right):
                res.append(right[j])
                j+=1
            return res
        nums=mergeSort(nums)
        res=[]
        n=len(nums)
        i=0
        while i<n-2:
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            l=i+1
            r=n-1
            while l<r:
                total=nums[i]+nums[l]+nums[r]
                if total==0:
                    res.append([nums[i],nums[l],nums[r]])
                    leftValue=nums[l]
                    rightValue=nums[r]
                    while l<r and nums[l]==leftValue:
                        l+=1
                    while l<r and nums[r]==rightValue:
                        r-=1
                elif total<0:
                    l+=1
                else:
                    r-=1
            i+=1
        if len(res)==0:
            return None
        return res