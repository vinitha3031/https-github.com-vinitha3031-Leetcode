class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if i<j and nums[i]+nums[j]<target and j<len(nums):
                    count+=1
                
        return count
        