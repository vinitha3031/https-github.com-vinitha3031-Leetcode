class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        a=sorted(score)[::-1]
        ans=[]
        for i in score:
            b=a.index(i)
            if b+1==1:
                ans.append("Gold Medal")
            elif b+1==2:
                ans.append("Silver Medal")
            elif b+1==3:
                ans.append("Bronze Medal")
            else:
                ans.append(str(b+1))
        print(ans)
        return ans
        