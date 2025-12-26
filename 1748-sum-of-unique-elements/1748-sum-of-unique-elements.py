class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        a=Counter(nums)
        ans=[]
        for i,j in a.items():
            if j==1:
                ans.append(i)
        return sum(ans)
        