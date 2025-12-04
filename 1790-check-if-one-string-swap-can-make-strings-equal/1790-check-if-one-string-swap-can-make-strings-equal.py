class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if Counter(s1)!=Counter(s2):
            return False
        else:
            h={}
            c=0
            for i in range(len(s1)):
                h[i]=s1[i]
            for i in range(len(s2)):
                if h[i]!=s2[i]:
                    c+=1
                if c>2:
                    return False
            return True