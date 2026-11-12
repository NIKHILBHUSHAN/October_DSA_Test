class Solution:
    def firstUniqChar(self,nums:list[int])->int:
        """for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    count+=1
            if count==1:
                return nums[i]
        return -1"""
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for num in nums:
            if freq[num]==1:
                return num
        return -1