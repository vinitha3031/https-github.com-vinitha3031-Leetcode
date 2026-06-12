class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        cnt=0
        for i in arr1:
            c=True
            for j in arr2:
                if abs(i-j)<=d:
                    c=False
                    break
            if c:
                cnt+=1
        return cnt
                
        

        