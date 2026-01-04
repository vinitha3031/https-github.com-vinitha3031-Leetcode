class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans=[]
        for i in nums:
            a=set()
            for j in range(1,int(i**0.5)+1):
                if i%j==0:
                    a.add(j) 
                    a.add(i//j)
                if len(a)>4:
                    break
            if len(a)==4:
                ans.append(sum(a))
        return sum(ans)