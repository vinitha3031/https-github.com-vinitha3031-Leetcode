class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        ans=0
        sub=""
        while r<len(s):
            while s[r] in sub:
                l+=1
                sub=s[l:r]
            sub+=s[r]
            ans=max(ans,r-l+1)
            r+=1
        print(sub,r,l)
        return ans


        