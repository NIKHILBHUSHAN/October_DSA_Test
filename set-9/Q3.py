'''class Solution:
    def intersection(self,A,B):
        result=[]
        for i in range(len(A)):
            found=False
            for j in range(len(B)):
                if A[i]==B[j]:
                    found=True
                    break
            if found:
                duplicate=False
                for j in range(len(result)):
                    if result[j]==A[i]:
                        duplicate=True
                        break
                if not duplicate:
                    result.append(A[i])
        for i in range(len(result)):
            smallest=i
            for j in range(i+1,len(result)):
                if result[j]<result[smallest]:
                    smallest=j
            temp=result[i]
            result[i]=result[smallest]
            result[smallest]=temp
        if len(result)==0:
            return None
        return result
'''
class Solution:
    def intersection(self,A,B):
        seen=set()
        common=set()
        for i in range(len(A)):
            seen.add(A[i])
        for i in range(len(B)):
            if B[i] in seen:
                common.add(B[i])
        result=[]
        for x in common:
            result.append(x)
        if len(result)==0:
            return None
        temp=[0]*len(result)
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
                if result[i]<=result[j]:
                    temp[k]=result[i]
                    i+=1
                else:
                    temp[k]=result[j]
                    j+=1
                k+=1
            while i<=mid:
                temp[k]=result[i]
                i+=1
                k+=1
            while j<=right:
                temp[k]=result[j]
                j+=1
                k+=1
            for i in range(left,right+1):
                result[i]=temp[i]
        merge_sort(0,len(result)-1)
        return result