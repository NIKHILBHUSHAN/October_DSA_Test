class Solution:
    def findKthLargest(self,nums:list[int],k:int)->int:
        """
        n=len(nums)
        for i in range(k):
            max_index=i
            for j in range(i+1,n):
                if nums[j]>nums[max_index]:
                    max_index=j
            nums[i],nums[max_index]=nums[max_index],nums[i]
        return nums[k-1]
        """
        target=k-1
        left=0
        right=len(nums)-1
        while left<=right:
            pivot=nums[right]
            i=left
            for j in range(left,right):
                if nums[j]>pivot:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
            nums[i],nums[right]=nums[right],nums[i]
            if i==target:
                return nums[i]
            elif i<target:
                left=i+1
            else:
                right=i-1