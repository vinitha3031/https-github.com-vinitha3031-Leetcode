class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        a=len(matrix)
        b=len(matrix[0])
        c=[[0]*a for i in range(b)]
        for i in range(a):
            for j in range(b):
                c[j][i]=matrix[i][j] 
        print(c)
        return c