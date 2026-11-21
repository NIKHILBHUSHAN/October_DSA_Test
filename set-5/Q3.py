class Solution:
    def insertionSort(self,nums:list[int])->tuple[list[int],int]:
        """
        n=len(nums)
        shifts=0
        for i in range(n):
            min_index=i
            for j in range(i+1,n):
                if nums[j]<nums[min_index]:
                    min_index=j
            while min_index>i:
                nums[min_index],nums[min_index-1]=nums[min_index-1],nums[min_index]
                min_index-=1
                shifts+=1
        return nums,shifts
        """
        shifts=0
        for i in range(1,len(nums)):
            key=nums[i]
            j=i-1
            while j>=0 and nums[j]>key:
                nums[j+1]=nums[j]
                j-=1
                shifts+=1
            nums[j+1]=key
        return nums,shifts