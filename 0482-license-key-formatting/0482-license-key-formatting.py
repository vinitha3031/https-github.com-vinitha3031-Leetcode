class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        a=s.split("-")
        b="".join(a)
        ans=""
        c=b[::-1]
        for i in range(0,len(b),k):
            ans+=c[i:i+k].upper()+"-"
        print(ans[::-1])
        return ans[::-1][1:]