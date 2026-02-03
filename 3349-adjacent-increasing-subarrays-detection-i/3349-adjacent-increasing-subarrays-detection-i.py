class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        i=0
        while i+(k*2)<=len(nums):
            a=nums[i:i+k]
            b=nums[i+k:i+(k*2)]
            if (sorted(a)==a and len(set(a))==k) and (sorted(b)==b and len(set(b))==k):
                return True
            i+=1
        return False
           