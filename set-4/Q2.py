class Solution:
    def containsNearbyDuplicate(self,nums:list[int],k:int)->bool:
        """for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and j-i<=k:
                    return True
        return False"""
        last_seen={}
        for i in range(len(nums)):
            if nums[i] in last_seen and i-last_seen[nums[i]]<=k:
                return True
            last_seen[nums[i]]=i
        return False