class Solution:
    def selectionSort(self,nums:list[int],k:int)->list[int]:
        """
        n=len(nums)
        for i in range(n):
            min_index=i
            for j in range(i+1,n):
                if nums[j]<nums[min_index]:
                    min_index=j
            nums[i],nums[min_index]=nums[min_index],nums[i]
        return nums[:k]
        """
        n=len(nums)
        for i in range(k):
            min_index=i
            for j in range(i+1,n):
                if nums[j]<nums[min_index]:
                    min_index=j
            nums[i],nums[min_index]=nums[min_index],nums[i]
        return [nums[i] for i in range(k)]