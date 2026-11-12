class Solution:
    def longestStreak(self,attendance:list[int],threshold:int)->int:
        """max_length=0
        for i in range(len(attendance)):
            if attendance[i]>=threshold:
                count=0
                for j in range(i,len(attendance)):
                    if attendance[j]>=threshold:
                        count+=1
                    else:
                        break
                if count>max_length:
                    max_length=count
        return max_length"""
        current_length=0
        max_length=0
        for num in attendance:
            if num>=threshold:
                current_length+=1
                if current_length>max_length:
                    max_length=current_length
            else:
                current_length=0
        return max_length