class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count=0
        i=0
        while i+3<=len(s):
            a=s[i:i+3]
            if len(a)==len(set(a)):
                count+=1
            i+=1
        print(count)
        return count