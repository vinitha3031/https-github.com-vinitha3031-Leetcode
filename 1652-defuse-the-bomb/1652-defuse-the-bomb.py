class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n=len(code)
        res=[]
        for i in range(n):
            total=0
            for j in range(1,abs(k)+1):
                if k<0:
                    a=(i-j)%n
                else:
                    a=(i+j)%n
                total+=code[a]
            res.append(total)
        return res
        