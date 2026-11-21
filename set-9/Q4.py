'''class Solution:
    def merge(self,intervals):
        arr=[]
        for i in range(len(intervals)):
            arr.append([intervals[i][0],intervals[i][1]])
        n=len(arr)
        for i in range(1,n):
            key=arr[i]
            j=i-1
            while j>=0 and arr[j][0]>key[0]:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key
        result=[]
        for i in range(n):
            if len(result)==0 or arr[i][0]>result[len(result)-1][1]:
                result.append([arr[i][0],arr[i][1]])
            else:
                if arr[i][1]>result[len(result)-1][1]:
                    result[len(result)-1][1]=arr[i][1]
        return result
'''
class Solution:
    def merge(self,intervals):
        arr=[]
        for i in range(len(intervals)):
            arr.append([intervals[i][0],intervals[i][1]])
        temp=[None]*len(arr)
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
                if arr[i][0]<arr[j][0] or (arr[i][0]==arr[j][0] and arr[i][1]<=arr[j][1]):
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
        result=[]
        for i in range(len(arr)):
            if len(result)==0 or arr[i][0]>result[len(result)-1][1]:
                result.append([arr[i][0],arr[i][1]])
            else:
                if arr[i][1]>result[len(result)-1][1]:
                    result[len(result)-1][1]=arr[i][1]
        return result