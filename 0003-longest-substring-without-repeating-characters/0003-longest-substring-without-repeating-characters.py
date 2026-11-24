class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        ans=0
        sub=set()
        while r<len(s):
            while s[r] in sub:
                sub.remove(s[l])
                l+=1
            sub.add(s[r])
            ans=max(ans,r-l+1)
            r+=1
        return ans


        