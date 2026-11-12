class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans=[]
        total=0
        for i in nums:
            total+=i
            ans.append(total)
        return ans
        