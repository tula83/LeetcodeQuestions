#finding anagrams in two string
class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(s)<len(p):
            return  []
        
        n,m=len(s),len(p)
        p=sorted(p)
        ans=list()

        for i in range(n-m+1):
            sub_string=s[i:m+i]
            sub_string=sorted(sub_string)
            if sub_string==p:
                ans.append(i)
                i+=m
            
        return ans



        