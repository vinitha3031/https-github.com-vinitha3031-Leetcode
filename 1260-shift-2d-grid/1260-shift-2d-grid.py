class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        while k:
            a=[[0]*n for x in range(m)]
            for i in range(m):
                for j in range(n):
                    if j==n-1:
                        if i==m-1:
                            a[0][0]=grid[i][j]
                        else:
                            a[i+1][0]=grid[i][j] 
                    else:
                        a[i][j+1]=grid[i][j]
            grid=a
            k-=1
        print(grid)
        return grid
        