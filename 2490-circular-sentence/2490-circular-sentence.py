class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        b=sentence.split()
        if len(b)==1:
            return sentence[-1]==sentence[0]
        a=b[0][-1]
        for i in b[1:]:
            if a!=i[0]:
               return False
            a=i[-1]
        return a==b[0][0]
           