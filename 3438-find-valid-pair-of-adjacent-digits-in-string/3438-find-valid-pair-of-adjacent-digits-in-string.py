from collections import Counter
class Solution:
    def findValidPair(self, s: str) -> str:
        h=Counter(s)
        for i in range(0,len(s)-1):
            if s[i]!=s[i+1]:
                if int(s[i])==h[s[i]] and int(s[i+1])==h[s[i+1]]:
                    return s[i]+s[i+1]
        return ""

                
