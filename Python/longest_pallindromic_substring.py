class Solution:
    def longestPalindrome(self, given: str) -> str:
       
        ans=[]
        if len(given)<=1:
            return given
        for i in range(len(given)-1):
            for j in range(i+1,len(given)):
                original_string=given[i:j+1]
                temp=original_string[::-1]
                if temp==original_string:
                    ans.append(temp)
        if len(ans)==0:
            return  given[0]
        return max(ans,key=len)
        



        