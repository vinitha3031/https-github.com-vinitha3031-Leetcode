class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        b=0
        for i in range(len(s)):
            if s[i]=="1":
                b+=1
            if s[i]=="0" and b:
                if "1" in s[i:]:
                    return False
        return True
