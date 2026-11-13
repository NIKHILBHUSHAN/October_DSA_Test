class Solution:
    def lengthOfLongestSubstring(self,nums:list[int])->int:
        """max_length=0
        for i in range(len(nums)):
            seen=set()
            current_length=0
            for j in range(i,len(nums)):
                if nums[j] in seen:
                    break
                seen.add(nums[j])
                current_length+=1
            if current_length>max_length:
                max_length=current_length
        return max_length"""
        last_seen={}
        left=0
        max_length=0
        for right in range(len(nums)):
            if nums[right] in last_seen and last_seen[nums[right]]>=left:
                left=last_seen[nums[right]]+1
            last_seen[nums[right]]=right
            current_length=right-left+1
            if current_length>max_length:
                max_length=current_length
        return max_length