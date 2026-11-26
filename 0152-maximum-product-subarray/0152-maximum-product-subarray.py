class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        premin=nums[0]
        premax=nums[0]
        ans=nums[0]

        for i in range(1,len(nums)):
            currmin=min(nums[i],nums[i]*premin,nums[i]*premax)
            currmax=max(nums[i],nums[i]*premin,nums[i]*premax)

            premin=currmin
            premax=currmax

            ans=max(ans,premax)
        return ans



        
                
       
                