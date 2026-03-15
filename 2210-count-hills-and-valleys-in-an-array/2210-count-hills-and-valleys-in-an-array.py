class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            a=0
            b=0
            for j in nums[:i][::-1]:
                if nums[i]!=j:
                    a=j
                    break  
            for k in nums[i+1:]:
                if nums[i]!=k:
                    b=k
                    break
            if a and b:
                if (nums[i]<a and nums[i]<b) or (nums[i]>b and nums[i]>a):
                    count+=1
        print(count)
        return count

