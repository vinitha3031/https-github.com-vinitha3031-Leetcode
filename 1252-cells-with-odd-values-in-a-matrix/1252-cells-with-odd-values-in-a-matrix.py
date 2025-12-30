class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        a=[[0]*n for i in range(m)]
        ans=0
        for i in indices:
            for j in range(n):
                a[i[0]][j]+=1
                if a[i[0]][j]%2!=0:
                    ans+=1
                else:
                    ans-=1
            for k in range(m):
                a[k][i[1]]+=1
            
                if a[k][i[1]]%2!=0:
                    ans+=1
                else:
                    ans-=1
        return ans

        
            