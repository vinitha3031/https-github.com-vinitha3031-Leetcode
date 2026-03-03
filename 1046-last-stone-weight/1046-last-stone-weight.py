class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        a=sorted(stones)
        while len(a)!=1:
            a.sort()
            b=a[-1]-a[-2]
            a.pop()
            a.pop()
            a.append(b)
        print(a[0])
        return a[0]

