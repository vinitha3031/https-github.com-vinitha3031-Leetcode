class Solution:
    def getLucky(self, s: str, k: int) -> int:
        a=""
        ans=0
        for i in s:
            a+=str(ord(i)-ord("a")+1)
        while k:
            ans=0
            for i in a:
                ans+=int(i)
            a=str(ans)
            k-=1
        print(ans)
        return ans

        