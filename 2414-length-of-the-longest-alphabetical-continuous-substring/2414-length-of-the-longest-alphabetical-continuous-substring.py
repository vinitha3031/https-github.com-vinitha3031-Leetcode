class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        c=1
        a=s[0]
        ans=[]
        for i in s[1:]:
            if chr(ord(a)+1)==i:
                a=i
                c+=1
            else:
                ans.append(c)
                c=1
                a=i
        if c:
            ans.append(c)
        print(ans)
        return max(ans)

            
        