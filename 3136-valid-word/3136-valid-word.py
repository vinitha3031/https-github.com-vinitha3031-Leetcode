class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        b=['a', 'e', 'i', 'o', 'u']
        c=list(set(a)-set(b))
        b1=False
        c1=False
        for i in word.lower():
            if i in b:
                b1=True
            elif i in c:
                c1=True
            elif not i.isalnum():
                return False
        return b1 and c1


        