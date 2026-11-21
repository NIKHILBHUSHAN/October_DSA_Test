'''class Solution:
    def shipWithinDays(self,weights,D):
        heaviest=weights[0]
        total=0
        for i in range(len(weights)):
            if weights[i]>heaviest:
                heaviest=weights[i]
            total+=weights[i]
        capacity=heaviest
        while capacity<=total:
            days=1
            current=0
            for i in range(len(weights)):
                if current+weights[i]<=capacity:
                    current+=weights[i]
                else:
                    days+=1
                    current=weights[i]
            if days<=D:
                return capacity
            capacity+=1
        return total
'''
class Solution:
    def shipWithinDays(self,weights,D):
        heaviest=weights[0]
        total=0
        for i in range(len(weights)):
            if weights[i]>heaviest:
                heaviest=weights[i]
            total+=weights[i]
        lo=heaviest
        hi=total
        ans=total
        while lo<=hi:
            mid=lo+(hi-lo)//2
            days=1
            current=0
            for i in range(len(weights)):
                if current+weights[i]<=mid:
                    current+=weights[i]
                else:
                    days+=1
                    current=weights[i]
            if days<=D:
                ans=mid
                hi=mid-1
            else:
                lo=mid+1
        return ans