class Solution:
    def reverseBits(self, n: int) -> int:
        a=format(n,"032b")
        b=a[::-1]
        return int(b,2)
        