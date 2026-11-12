class Solution:
    def secondHighest(self,nums:list[int])->int|None:
        """largest=None
        for num in nums:
            if largest is None or num>largest:
                largest=num
        second=None
        for num in nums:
            if num!=largest and (second is None or num>second):
                second=num
        return second"""
        largest=None
        second=None
        for num in nums:
            if largest is None or num>largest:
                second=largest
                largest=num
            elif num!=largest and (second is None or num>second):
                second=num
        return second