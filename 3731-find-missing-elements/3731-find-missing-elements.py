class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        a=list(i for i in range(nums[0],nums[-1]+1))
        ans=[]
        for i in a:
            if i not in nums:
                ans.append(i)
        return ans
                
