class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ans=0
        a=sorted([i[0] for i in points])
        for i in range(len(a)-1):
            b=abs(a[i]-a[i+1])
            if ans<b:
                ans=b
        return ans
            
            