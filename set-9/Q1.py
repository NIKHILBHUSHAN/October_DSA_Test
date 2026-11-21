'''class Solution:
    def twoSum(self,prices,T):
        n=len(prices)
        for i in range(n):
            for j in range(i+1,n):
                if prices[i]+prices[j]==T:
                    return [i+1,j+1]
        return []
'''
class Solution:
    def twoSum(self,prices,T):
        left=0
        right=len(prices)-1
        while left<right:
            total=prices[left]+prices[right]
            if total==T:
                return [left+1,right+1]
            elif total<T:
                left+=1
            else:
                right-=1
        return []