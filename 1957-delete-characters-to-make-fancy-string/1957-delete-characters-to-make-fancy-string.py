class Solution:
    def makeFancyString(self, s: str) -> str:
        a=s[0]
        b=1
        ans=s[0]
        for i in s[1:]:
            if a!=i:
                ans+=i
                a=i
                b=1
            elif a==i and b>1:
                b+=1
                continue
            else:
                b+=1
                ans+=i
        return ans

        