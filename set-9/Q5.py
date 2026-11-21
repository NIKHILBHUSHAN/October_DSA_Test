'''class Solution:
    def insert(self,intervals,newInterval):
        arr=[]
        for i in range(len(intervals)):
            arr.append([intervals[i][0],intervals[i][1]])
        arr.append([newInterval[0],newInterval[1]])
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
    def insert(self,intervals,newInterval):
        result=[]
        i=0
        n=len(intervals)
        start=newInterval[0]
        end=newInterval[1]
        while i<n and intervals[i][1]<start:
            result.append([intervals[i][0],intervals[i][1]])
            i+=1
        while i<n and intervals[i][0]<=end:
            if intervals[i][0]<start:
                start=intervals[i][0]
            if intervals[i][1]>end:
                end=intervals[i][1]
            i+=1
        result.append([start,end])
        while i<n:
            result.append([intervals[i][0],intervals[i][1]])
            i+=1
        return result