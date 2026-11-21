class Solution:
    def bubbleSort(self,nums:list[int])->tuple[list[int],int]:
        """
        n=len(nums)
        for i in range(n-1):
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums
        """
        n=len(nums)
        productive_passes=0
        for i in range(n-1):
            swapped=False
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                    swapped=True
            if swapped:
                productive_passes+=1
            else:
                break
        return nums,productive_passes