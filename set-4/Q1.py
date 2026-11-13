class Solution:
    def maxSum(self,nums:list[int],k:int)->int:
        """max_sum=float('-inf')
        for i in range(len(nums)-k+1):
            current_sum=0
            for j in range(i,i+k):
                current_sum+=nums[j]
            if current_sum>max_sum:
                max_sum=current_sum
        return max_sum"""
        window_sum=0
        for i in range(k):
            window_sum+=nums[i]
        max_sum=window_sum
        for i in range(k,len(nums)):
            window_sum+=nums[i]-nums[i-k]
            if window_sum>max_sum:
                max_sum=window_sum
        return max_sum