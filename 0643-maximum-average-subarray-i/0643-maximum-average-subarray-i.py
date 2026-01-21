class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        j=k
        sums=sum(nums[i:j])
        t=sums
        while j<len(nums):
            t=t-nums[i]+nums[j]
            if t>sums:
                sums=t
            i+=1
            j+=1         
        return sums/k    
