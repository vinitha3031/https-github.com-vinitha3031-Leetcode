class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            a=""
            for i in range(0,len(s),k):
                b=s[i:i+k]
                c=list(map(int,b))
                a+=str(sum(c))
            s=a
        return s

                
                
        