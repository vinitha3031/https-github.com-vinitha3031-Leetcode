class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        a=[i for i in range(len(nums)) if nums[i]==key]
        ans=[]
        for i in range(len(nums)):
            for j in a:
                if abs(i-j)<=k:
                    ans.append(i)
                    break
        print(ans)
        return ans
        