class Solution:
    def rotate(self,nums:list[int],k:int)->None:
        """k=k%len(nums)
        for _ in range(k):
            last=nums[len(nums)-1]
            i=len(nums)-1
            while i>0:
                nums[i]=nums[i-1]
                i-=1
            nums[0]=last"""
        n=len(nums)
        k=k%n
        def reverse(left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)