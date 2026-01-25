class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        i=1
        while i<n:
            a=i
            b=n-i
            if "0" not in str(a) and "0" not in str(b) and a+b==n:
                return [a,b]
            i+=1

