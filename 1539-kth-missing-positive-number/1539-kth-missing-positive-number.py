class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        c=1
        while k:
            if c not in arr:
                k-=1
            c+=1
        print(c)
        return c-1
        