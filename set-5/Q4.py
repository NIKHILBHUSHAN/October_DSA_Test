class Solution:
    def inversionCount(self,nums:list[int])->int:
        """
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    count+=1
        return count
        """
        def merge_sort(left,right):
            if left>=right:
                return 0
            mid=(left+right)//2
            count=merge_sort(left,mid)
            count+=merge_sort(mid+1,right)
            temp=[]
            i=left
            j=mid+1
            while i<=mid and j<=right:
                if nums[i]<=nums[j]:
                    temp.append(nums[i])
                    i+=1
                else:
                    temp.append(nums[j])
                    count+=mid-i+1
                    j+=1
            while i<=mid:
                temp.append(nums[i])
                i+=1
            while j<=right:
                temp.append(nums[j])
                j+=1
            for i in range(len(temp)):
                nums[left+i]=temp[i]
            return count
        return merge_sort(0,len(nums)-1)