class Solution:
    def allocateBooks(self,pages,m):
        '''
        n=len(pages)
        if m>n:
            return -1
        low=pages[0]
        high=0
        for x in pages:
            if x>low:
                low=x
            high+=x
        capacity=low
        while capacity<=high:
            groups=1
            current=0
            for x in pages:
                if current+x>capacity:
                    groups+=1
                    current=x
                else:
                    current+=x
            if groups<=m:
                return capacity
            capacity+=1
        return -1
        '''
        n=len(pages)
        if m>n:
            return -1
        low=pages[0]
        high=0
        for x in pages:
            if x>low:
                low=x
            high+=x
        ans=high
        while low<=high:
            mid=low+(high-low)//2
            groups=1
            current=0
            for x in pages:
                if current+x>mid:
                    groups+=1
                    current=x
                else:
                    current+=x
            if groups<=m:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans