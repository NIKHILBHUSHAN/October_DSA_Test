class Solution:
    def isPalindrome(self,s:str)->bool:
        """cleaned=""
        for ch in s:
            if ch.isalnum():
                cleaned+=ch.lower()
        reversed_string=""
        for i in range(len(cleaned)-1,-1,-1):
            reversed_string+=cleaned[i]
        return cleaned==reversed_string"""
        left=0
        right=len(s)-1
        while left<right:
            while left<right and not s[left].isalnum():
                left+=1
            while left<right and not s[right].isalnum():
                right-=1
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True