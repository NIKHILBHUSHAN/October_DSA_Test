class Solution:
    def reverseVowels(self,s:str)->str:
        """vowels=[]
        for ch in s:
            if ch in "aeiouAEIOU":
                vowels.append(ch)
        result=""
        index=len(vowels)-1
        for ch in s:
            if ch in "aeiouAEIOU":
                result+=vowels[index]
                index-=1
            else:
                result+=ch
        return result"""
        chars=list(s)
        left=0
        right=len(chars)-1
        vowels="aeiouAEIOU"
        while left<right:
            while left<right and chars[left] not in vowels:
                left+=1
            while left<right and chars[right] not in vowels:
                right-=1
            chars[left],chars[right]=chars[right],chars[left]
            left+=1
            right-=1
        return "".join(chars)