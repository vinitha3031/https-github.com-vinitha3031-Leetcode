class Solution:
    def possibleStringCount(self, word: str) -> int:
        a=word[0]
        c=0
        for i in word[1:]:
            if a==i:
                c+=1
            if a!=i:
                a=i
        print(c)
        return c+1
