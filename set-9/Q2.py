'''class Solution:
    def trimmedMean(self,scores,t):
        arr=[]
        for i in range(len(scores)):
            arr.append(scores[i])
        n=len(arr)
        for i in range(n):
            for j in range(n-i-1):
                if arr[j]>arr[j+1]:
                    temp=arr[j]
                    arr[j]=arr[j+1]
                    arr[j+1]=temp
        total=0
        for i in range(t,n-t):
            total+=arr[i]
        count=n-2*t
        scaled=total*100
        rounded=(scaled*2+count)//(2*count)
        whole=rounded//100
        decimal=rounded%100
        result=str(whole)+"."
        if decimal<10:
            result+="0"
        result+=str(decimal)
        return result
'''
class Solution:
    def trimmedMean(self,scores,t):
        arr=[]
        for i in range(len(scores)):
            arr.append(scores[i])
        temp=[0]*len(arr)
        def merge_sort(left,right):
            if left>=right:
                return
            mid=(left+right)//2
            merge_sort(left,mid)
            merge_sort(mid+1,right)
            i=left
            j=mid+1
            k=left
            while i<=mid and j<=right:
                if arr[i]<=arr[j]:
                    temp[k]=arr[i]
                    i+=1
                else:
                    temp[k]=arr[j]
                    j+=1
                k+=1
            while i<=mid:
                temp[k]=arr[i]
                i+=1
                k+=1
            while j<=right:
                temp[k]=arr[j]
                j+=1
                k+=1
            for i in range(left,right+1):
                arr[i]=temp[i]
        merge_sort(0,len(arr)-1)
        total=0
        n=len(arr)
        for i in range(t,n-t):
            total+=arr[i]
        count=n-2*t
        scaled=total*100
        rounded=(scaled*2+count)//(2*count)
        whole=rounded//100
        decimal=rounded%100
        result=str(whole)+"."
        if decimal<10:
            result+="0"
        result+=str(decimal)
        return result