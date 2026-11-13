class Solution:
    def numOfStrongWindows(self,nums:list[int],k:int,T:int)->int:
        """count=0
        for i in range(len(nums)-k+1):
            current_sum=0
            for j in range(i,i+k):
                current_sum+=nums[j]
            if current_sum>=k*T:
                count+=1
        return count"""
        window_sum=0
        count=0
        for i in range(k):
            window_sum+=nums[i]
        if window_sum>=k*T:
            count+=1
        for i in range(k,len(nums)):
            window_sum+=nums[i]-nums[i-k]
            if window_sum>=k*T:
                count+=1
        return count