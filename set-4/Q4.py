class Solution:
    def findAnagrams(self,s:str,p:str)->list[int]:
        """result=[]
        m=len(p)
        for i in range(len(s)-m+1):
            freq1={}
            freq2={}
            for j in range(m):
                if s[i+j] in freq1:
                    freq1[s[i+j]]+=1
                else:
                    freq1[s[i+j]]=1
                if p[j] in freq2:
                    freq2[p[j]]+=1
                else:
                    freq2[p[j]]=1
            if freq1==freq2:
                result.append(i)
        return result"""
        n=len(s)
        m=len(p)
        if m>n:
            return []
        p_freq=[0]*26
        window_freq=[0]*26
        for i in range(m):
            p_freq[ord(p[i])-ord('a')]+=1
            window_freq[ord(s[i])-ord('a')]+=1
        result=[]
        if p_freq==window_freq:
            result.append(0)
        for i in range(m,n):
            window_freq[ord(s[i])-ord('a')]+=1
            window_freq[ord(s[i-m])-ord('a')]-=1
            if p_freq==window_freq:
                result.append(i-m+1)
        return result