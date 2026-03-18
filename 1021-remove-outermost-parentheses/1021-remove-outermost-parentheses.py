class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=""
        a=0
        for i in range(len(s)):
            if s[i]=="(":
                if a>0:
                    ans+=s[i]
                a+=1
            if s[i]==")":
                a-=1
                if a>0:
                    ans+=s[i]
        return ans
            
            