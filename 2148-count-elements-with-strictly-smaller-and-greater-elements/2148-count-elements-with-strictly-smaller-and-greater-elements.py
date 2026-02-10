class Solution:
    def countElements(self, nums: List[int]) -> int:
        a=max(nums)
        b=min(nums)
        cnt=0
        for i in nums:
            if i<a and i>b:
                cnt+=1
        print(cnt)
        return cnt
        