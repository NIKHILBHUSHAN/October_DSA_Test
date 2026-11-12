class Solution:
    def firstDuplicate(self,nums:list[int])->int:
        """for i in range(len(nums)):
            for j in range(i):
                if nums[i]==nums[j]:
                    return nums[i]
        return -1"""
        seen=set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1