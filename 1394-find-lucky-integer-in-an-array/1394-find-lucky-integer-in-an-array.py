class Solution:
    def findLucky(self, arr: List[int]) -> int:
        a=Counter(arr)
        print(a)
        ans=[]
        for i,j in a.items():
            if i==j:
                ans.append(i)
        print(ans)
        if ans:
            return max(ans)
        return -1

        