class Solution:
    def rangeSum(self,nums:list[int],queries:list[list[int]])->list[int]:
        """results=[]
        for l,r in queries:
            total=0
            for i in range(l,r+1):
                total+=nums[i]
            results.append(total)
        return results"""
        prefix=[0]
        for num in nums:
            prefix.append(prefix[-1]+num)
        results=[]
        for l,r in queries:
            results.append(prefix[r+1]-prefix[l])
        return results