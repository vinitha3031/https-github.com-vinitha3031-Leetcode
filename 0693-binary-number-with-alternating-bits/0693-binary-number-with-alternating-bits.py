class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        ans=True
        a=bin(n)[2:]
        for i in range(1,len(a)):
            if a[i]==a[i-1]:
                return False
        return ans
        