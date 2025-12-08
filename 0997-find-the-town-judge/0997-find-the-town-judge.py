class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a=[]
        b=[]
        for i in trust:
            a.append(i[0])
            b.append(i[1])
        for i in range(1,n+1):
            if a.count(i)==0 and  b.count(i)==n-1:
                return i
        return -1       
        