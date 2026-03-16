class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        a=0
        for i in range(len(nums)):
            b=True
            if i-k>=0 and nums[i-k]>=nums[i]:
                b=False
            if i+k<len(nums) and nums[i+k]>=nums[i]:
               b=False
            if b:
                a+=nums[i]
        return a
        