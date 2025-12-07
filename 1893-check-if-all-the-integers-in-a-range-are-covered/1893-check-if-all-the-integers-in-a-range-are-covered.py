class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left,right+1):
            c=0
            for j in ranges:
                if j[0]<= i <=j[1]:
                    break
                else:
                    c+=1
            if c==len(ranges):
                return False
        return True

                

                    