class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        a=""
        b=""
        c=""
        d=""
        for i in range(len(s1)):
            if i%2!=0:
                a+=s1[i]
                c+=s2[i]
            else:
                b+=s1[i]
                d+=s2[i]
        return sorted(a)==sorted(c) and sorted(b)==sorted(d)
        